"""Monte Carlo simulation of a repeater chain with nondeterministic swapping and memory buffer in the doubling scheme.

The script performs a number of simulation runs, each of which corresponds
to the distribution of a single entangled pair of qubits between the end nodes
of the repeater chain. For each run, it prints the waiting time. The parameters of the simulation can be
changed at the bottom of this file.

Date: 16 Dec 2022
Author: Lina



Code explanation
================

The architecture
----------------

The repeater chain looks like this:

1  2 3  4 5  6 7  8
+  + +  + +  + +  +  step 0
+--+ +--+ +--+ +--+  step 1
+-------+ +-------+  step 2
+-----------------+  step 3

where each '+' is a node/ memory and '--' is a link. Initially, we are in step 0 with no existing links. With a fixed generation probability, we generate a link. Once we have two links prepared, we can swap to get a longer link. Swapping happens with a fixed swapping probability. Swapping is only allowed at nodes (2,3) and (6,7) in step 1 or at node (4,5) in step 2. (Doubling scheme.) 
Some nodes have a memory buffer, so that new links of step 1 can get prepared, while the link in step 2 is waiting for the second link




The protocol
------------

The protocol that this script currently implements is as follows:
In each timestep, 
- over each connection in step 0 which has free memories, elementary-link generation is attempted
- as soon as two links are prepared, swapping is attempted. Note, that swapping is only allowed between some links, see picture above.

As soon as there is a single elementary link between the end nodes, the simulation stops and output the number of timesteps.


Ideas for later
---------------
- add cutoff time
- add fidelity
"""

import numpy as np
import statistics
from math import comb


################################################################
# CLASSES FOR A MEMORY; ELEMENTARY_LINK, LONG_LINK, CHAIN;     #
# - an elementary link gets generated with a fixed probability #
# - a long link gets generated by swapping                     #
# - the chain reflects the structure, e.g. doubling scheme     #
################################################################



class Memory:
    """Class modelling an memory.
    Intended usage: the memory has a certain buffer space. 
    It keeps track of how many memories are occupied.
    'occupy_memory' and 'free_memory' occupies or frees memory space.
    In case we try to occupy more memory space than available 
    or we try to free an empty memory, it outputs an error message.
    'evaluate_full' checks, whether the memory buffer is full, 
    i.e. there is no free memory space left, 
    what means that we can't generate more links


    Parameters
    ----------
    buffer_space: int
        The number of available memory space, occupied or not.
    _occupied_buffer_space: int
        The number of occupied buffer space,
        can't be greater than buffer_space.
    _full_status: bool
        States whether the memory buffer is full or not.
    """

        
    def __init__(self,
                 buffer_space=1):
        self.buffer_space = buffer_space
        self._occupied_buffer_space = 0
        self._full_status = False


    def occupy_memory(self):
        """occupies memory space"""
        if self._full_status:
            raise Exception("Something went wrong: tried to occupy more space than possible")
        else:
            self._occupied_buffer_space += 1
        self.evaluate_full()

    def free_memory(self):
        """frees memory space"""
        if self._occupied_buffer_space == 0:
            raise Exception("Something went wrong: tried to free memory space although it was free before")
        else:
            self._occupied_buffer_space -= 1
        self.evaluate_full()

    def evaluate_full(self):
        """checks, whether the memory buffer is full"""
        if self._occupied_buffer_space == self.buffer_space:
            self._full_status=True
        else:
            self._full_status=False



class Elementary_Link:
    """Class modelling an elementary link.
    Intended usage: an elementary link can exist or not.
    Added feature: they can have a _multiplicity (multiplexing).
    It needs two memories to get stored.
    If there is a free memory at each end, it attempts to get generated.
    Generation happens with a fixed generation probability.
    Ones it gets generated, it occupies memories on both sides.
    #include later: cutoff time


    Parameters
    ----------
    generation_probability: float
        Probability to generate a link.
    _is_working: bool
        States whether the link is generated or not
    memoryL, memoryR: Memory
        Memories on both sides of the link
    _ready_for_generation: bool
        States whether there is free memory space 
        such that a link can get generated.
    _multiplicity: int
        as long as we have sufficiently much buffer space, we can have multiple parallel links (multiplexing).
    """

    def __init__(self,
                 memoryL,
                 memoryR,
                 generation_probability=1):
        self.generation_probability = generation_probability
        self.memoryL = memoryL
        self.memoryR = memoryR
        self._ready_for_generation = False
        self._is_working = False
        self._multiplicity = 0
        



    def check_buffer_space(self):
        """checks whether there is enough memory buffer to generate a link"""
        #print(self.memoryL._full_status, self.memoryR._full_status)
        if not self.memoryL._full_status and not self.memoryR._full_status:
            self._ready_for_generation = True
        else: 
            self._ready_for_generation = False

    def generation_attempt(self):
        """attempts to generate an entangled link"""
        self.check_buffer_space()
        if self._ready_for_generation:
            if np.random.random() < self.generation_probability:
                #print("link generated")
                self.turn_on()


    def turn_on(self):
        """mark, that link is working and occupy memory space"""
        self._is_working = True
        self._multiplicity +=1
        self.memoryL.occupy_memory()
        self.memoryR.occupy_memory()


    def turn_off(self):
        """turns off existing"""
        if self._is_working:
            self._multiplicity -= 1
            self.memoryL.free_memory()
            self.memoryR.free_memory()
            """Note: if swapping was successfull, memories need to get occupied again."""
            if self._multiplicity == 0:
                self._is_working = False
        else:
            raise Exception("Something went wrong, tried to turn off a non working link.")


    def next_timestep(self):
        #if not self._is_working:
        self.generation_attempt()


class Long_Link:
    """Class modelling an long link generated by swapping.
    Intended usage: a long link can exist or not.
    Added feature: they can have a _multiplicity (multiplexing).
    It occupies one memory on each side.
    It can get generated by entanglement swapping if specific shorter links are working.
    Swapping happens with a fixed swapping probability.
    #include later: cutoff time


    Parameters
    ----------
    swapping_probability: float
        Probability to swap two links.
    _is_working: bool
        States whether the link is working or not
    link1, link2: Elementary_Link or Long_Link
    memoryL, memoryR: Memory
        Memories on both sides of the link
    _ready_for_swapping: bool
        States whether the shorter links are generated 
        such that they can get swapped.
    _multiplicity: int
        as long as we have sufficiently much buffer space, we can have multiple parallel links (multiplexing).
    _number_swapping_options: int
    """

    def __init__(self,
                 link1,
                 link2,
                 swapping_probability=1):
        self.swapping_probability = swapping_probability
        self.link1 = link1
        self.link2 = link2
        self.memoryL = self.link1.memoryL
        self.memoryR = self.link2.memoryR
        self._ready_for_swapping = False
        self._is_working = False
        self._multiplicity = 0
        self._number_swapping_options = 0

            
    def check_swapping_conditions(self):
        """checks whether the underlying links exist"""
        #print(self.link1._is_working, self.link2._is_working)
        if self.link1._is_working and self.link2._is_working:
            self._ready_for_swapping = True
            self._number_swapping_options = min(self.link1._multiplicity,self.link2._multiplicity)
            #print("multiplicities link1, link2: ", self.link1._multiplicity,self.link2._multiplicity)
            #print("_number_swapping_options: ", self._number_swapping_options)
        else: 
            self._ready_for_swapping = False  
            self._number_swapping_options = 0



    def swapping_attempt(self):
        """attempts to swap two entangled links"""
        self.check_swapping_conditions()
        #print("ready for swapping? ", self._ready_for_swapping)
        if self._ready_for_swapping:
            self.link1.turn_off()
            self.link2.turn_off()
            #print("turn off link1, link2: ", self.link1._is_working, self.link2._is_working)
            if np.random.random() < self.swapping_probability:
                self.turn_on()
                #print("swapping successful, _is_working: ", self._is_working)    

    def turn_on(self):
        """notice, that link is working and occupy memory space"""
        self._is_working = True
        self._multiplicity +=1
        self.memoryL.occupy_memory()
        self.memoryR.occupy_memory()  


    def turn_off(self):
        """turns off existing link"""
        if self._is_working:
            #self._is_working = False
            self._multiplicity -=1
            self.memoryL.free_memory()
            self.memoryR.free_memory()
            #print("longer link turned off: ", self._is_working)
            """Note: if swapping was successful, memories need to get occupied again."""
            if self._multiplicity == 0:
                self._is_working = False
        else:
            raise Exception("Something went wrong, tried to turn off a non working link.")

    def next_timestep(self):
        self.check_swapping_conditions()
        #print("_number_swapping_options: ", self._number_swapping_options) 
        number_of_attempts = self._number_swapping_options
        if self._number_swapping_options > 0:
            for __ in range(number_of_attempts):
                self.swapping_attempt()    
                #print("_multiplicity: ", self._multiplicity) 




class Chain:
    """Class modelling the chain.
    It contains all elementary and longer links. 
    Intended usage: Performs actions of time steps and compute waiting time.

    Parameters
    ----------
    links: array of arrays
        Links on each step of the protocol
    task_done: bool
        States whether task to generate a link between end nodes is done or not
    waiting_time: int 
    """

    def __init__(self,
                 links,
                 task_done=False,
                 waiting_time = 0):
        self.links = links
        self.task_done = task_done
        self.waiting_time = waiting_time

    def next_timestep(self):
        for i in range(len(self.links)):
        #for i in range(3):
            #print("step ", i)
            #j = 0
            for link in self.links[i]:
                #print("link ", j)
                #j += 1
                link.next_timestep()




    def evaluate_task_done(self):
        if self.links[-1][0]._is_working:
            self.task_done = True



    def find_waiting_time(self):
        self.waiting_time = 0
        while not self.task_done:
            self.waiting_time +=1
            self.next_timestep()
            self.evaluate_task_done()


 


#######################################
# METHODS FOR CREATING REPEATER CHAIN #
#######################################


def create_elementary_links(memory_numbers = np.full(8,1),
                            generation_probability=1):
    """creates a vector of elementary links with a distribution of memory_buffers"""

    if not len(memory_numbers) in [4,8,16,32,64]:
        raise Exception("Check length of memory_numbers, length is not appropriate for doubling scheme")


    linklist = []

    for i in range(int(len(memory_numbers)/2)):
        memoryL = Memory(buffer_space=memory_numbers[2*i])
        memoryR = Memory(buffer_space=memory_numbers[2*i+1])
        #print(memory_numbers[2*i])
        link = Elementary_Link(memoryL = memoryL, memoryR = memoryR,generation_probability=generation_probability)
        linklist.append(link)

    return(linklist)


def create_long_links_doubling(linklist_short,
                               swapping_probability=1):
    """creates a vector of longer links from a list of shorter links, doubling scheme"""

    if not len(linklist_short) in [2,4,8,16,32,64]:
        raise Exception("Check length of memory_numbers, length is not appropriate for doubling scheme")

    linklist = []

    for i in range(int(len(linklist_short)/2)):
        link1 = linklist_short[2*i]
        link2 = linklist_short[2*i+1]
        #print(memory_numbers[2*i])
        link = Long_Link(link1=link1,link2=link2,swapping_probability=swapping_probability)
        linklist.append(link)

    return(linklist)

    
def create_chain_doubling(memory_numbers = np.full(8,1),
                          generation_probability=1,
                          swapping_probability=1):    
    """creates a list of lists, where the first list element is a list of elementary links (step 1), the second list element is a list of longer links (step 2)..."""

    links = []
    #print(memory_numbers)
    linklist = create_elementary_links(memory_numbers=memory_numbers, generation_probability=generation_probability)
    links.append(linklist)

    while len(linklist) > 1:
        linklist = create_long_links_doubling(linklist, swapping_probability=swapping_probability)
        links.append(linklist)

    return links






###################################
# GET STATISTICS OF WAITING TIMES #
###################################


def get_statistics(memory_numbers = np.full(8,1),
                          generation_probability=1,
                          swapping_probability=1,
                          number_of_repetitions=100
                          ):

    waitingtimes = []
    chains = []

    for __ in range(number_of_repetitions):
        links = create_chain_doubling(memory_numbers = memory_numbers, 
                generation_probability=generation_probability,
                swapping_probability=swapping_probability)
        chain = Chain(links)
        chains.append(chain)

    for chain in chains: 
        chain.find_waiting_time()
        waitingtimes.append(chain.waiting_time)
    #print(waitingtimes, len(waitingtimes))
 
    mean = statistics.mean(waitingtimes)
    error = np.sqrt(statistics.variance(waitingtimes)/len(waitingtimes))


    #print("memory_buffer distribution: ", memory_numbers)
    #print("generation_probability: ", generation_probability , ", swapping_probability: ", swapping_probability)
    #print("waiting_time: ", mean, "+-", error)

    return [mean,error]


##################################################
# ENTERING PARAMETERS AND RUNNING THE SIMULATION #
##################################################


if __name__ == "__main__":

    """simulation parameters"""
    memory_numbers = [1,1,1,1,1,1,1,1]
    generation_probability=0.01
    swapping_probability=1
    number_of_repetitions=100   
    
    element_numbers = int(len(memory_numbers)/2) 

    data = get_statistics(memory_numbers = memory_numbers,
                          generation_probability=generation_probability,
                          swapping_probability=swapping_probability,
                          number_of_repetitions=number_of_repetitions)
                          
    print("simulation parameters: \n generation probability =  ", generation_probability, "\n swapping probability = ",swapping_probability , "\n repeater chain length: ", element_numbers)
    
    print("AWT simulation: ", data[0], "+-", data[1])
    

    print("analytic calculation for swapping_probability = 1 and memory_buffer = 1 at every repeater station:")
    n = element_numbers
    q = 1. - generation_probability
    expval = sum([(-1)**(j + 1)*comb(n,j)/(1-q**j) for j in range (1,n+1)])
    print("computed expectation value: ", expval)
