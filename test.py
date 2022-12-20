import memory_buffer_doubling as memb
import scipy.special
import numpy as np

"""Test of Memory"""
#print("Test of Memory")
#memory = memb.Memory(buffer_space=2)
#print("buffer space: ", memory.buffer_space)
#print("occupied buffer space: ", memory.occupied_buffer_space)
#print("full?", memory.full_status)
#memory.occupy_memory()
#print("occupied buffer space: ", memory.occupied_buffer_space)
#print("full?", memory.full_status)
#memory.occupy_memory()
#print("occupied buffer space: ", memory.occupied_buffer_space)
#print("full?", memory.full_status)
#memory.free_memory()
#print("occupied buffer space: ", memory.occupied_buffer_space)
#print("full?", memory.full_status)
#memory.free_memory()
#print("occupied buffer space: ", memory.occupied_buffer_space)
#print("full?", memory.full_status)

"""Test of Elementary Link"""
#print("Test of Elementary Link")
#elemlink = memb.Elementary_Link(memoryL = memb.Memory(buffer_space=3),memoryR = memb.Memory(buffer_space=2))
#print("working? ", elemlink.is_working)
#print("free memory space, L: ", elemlink.memoryL.buffer_space - elemlink.memoryL.occupied_buffer_space, "R: ", elemlink.memoryR.buffer_space - elemlink.memoryR.occupied_buffer_space)
#elemlink.check_buffer_space()
#print("ready for generation? ", elemlink.ready_for_generation)
#elemlink.generation_attempt()
#print("generation successful? ", elemlink.is_working)
#print("free memory space, L: ", elemlink.memoryL.buffer_space - elemlink.memoryL.occupied_buffer_space, "R: ", elemlink.memoryR.buffer_space - elemlink.memoryR.occupied_buffer_space)
#elemlink.check_buffer_space()
#print("ready for generation? ", elemlink.ready_for_generation)
#elemlink.turn_off()
#print("free memory space, L: ", elemlink.memoryL.buffer_space - elemlink.memoryL.occupied_buffer_space, "R: ", elemlink.memoryR.buffer_space - elemlink.memoryR.occupied_buffer_space)
#elemlink.turn_off()
#print("ready for generation? ", elemlink.ready_for_generation)
#print("working? ", elemlink.is_working)
#elemlink.next_timestep()
#print("working in next timestep? ", elemlink.is_working)




"""Test of Long Link"""
#print("Test of Long Link")
#link1 = memb.Elementary_Link(memoryL = memb.Memory(),memoryR = memb.Memory())
#link2 = memb.Elementary_Link(memoryL = memb.Memory(),memoryR = memb.Memory())
#llink = memb.Long_Link(link1=link1,link2=link2,swapping_probability=1)
#llink.check_swapping_conditions()
#print("free memory space, L: ", llink.memoryL.buffer_space - llink.memoryL.occupied_buffer_space, "R: ", llink.memoryR.buffer_space - llink.memoryR.occupied_buffer_space)
#print("ready for swapping? ", llink.ready_for_swapping)
#llink.link1.generation_attempt()
#llink.check_swapping_conditions()
#print("free memory space, L: ", llink.memoryL.buffer_space - llink.memoryL.occupied_buffer_space, "R: ", llink.memoryR.buffer_space - llink.memoryR.occupied_buffer_space)
#print("ready for swapping? ", llink.ready_for_swapping)
#llink.link2.generation_attempt()
#llink.check_swapping_conditions()
#print("free memory space, L: ", llink.memoryL.buffer_space - llink.memoryL.occupied_buffer_space, "R: ", llink.memoryR.buffer_space - llink.memoryR.occupied_buffer_space)
#print("ready for swapping? ", llink.ready_for_swapping)
#print("before next timestep, is working: ", llink.is_working)
#llink.next_timestep()
#print("next timestep, is working: ", llink.is_working)
#print("free memory space, L: ", llink.memoryL.buffer_space - llink.memoryL.occupied_buffer_space, "R: ", llink.memoryR.buffer_space - llink.memoryR.occupied_buffer_space)
#llink.turn_off()
#print("turn off, is working: ", llink.is_working)
#print("free memory space, L: ", llink.memoryL.buffer_space - llink.memoryL.occupied_buffer_space, "R: ", llink.memoryR.buffer_space - llink.memoryR.occupied_buffer_space)
#llink.check_swapping_conditions()
#print("xx ready for swapping? ", llink.ready_for_swapping)
#llink.link1.generation_attempt()
#llink.link2.generation_attempt()
#llink.check_swapping_conditions()
#print("xx ready for swapping? ", llink.ready_for_swapping)
#print("before next timestep, is working: ", llink.is_working)
#llink.next_timestep()
#print("next timestep, is working: ", llink.is_working)
#print("free memory space, L: ", llink.memoryL.buffer_space - llink.memoryL.occupied_buffer_space, "R: ", llink.memoryR.buffer_space - llink.memoryR.occupied_buffer_space)



"""Test of Chain Generation"""
#print("Test of Chain Generation - each step")
#memory_numbers = [3,1,1,3,3,1,1,3]
#linklist = memb.create_elementary_links(memory_numbers=memory_numbers)
#print("length of elementary linklist: ", len(linklist))
#linklist = memb.create_long_links_doubling(linklist, swapping_probability=1)
#print("length of longer linklist: ", len(linklist))
#linklist = memb.create_long_links_doubling(linklist, swapping_probability=1)
#print("length of longer linklist: ", len(linklist))
#print("Test of Chain Generation - combine")
#links = memb.create_chain_doubling()
#print("steps: ", len(links))
#print("length of elementary linklist: ", len(links[0]))
#print("length of longer linklist: ", len(links[1]))
#print("length of longer linklist: ", len(links[2]))
#print("links[0][0], is working: ", links[0][0].is_working)
#links[0][0].next_timestep()
#print("links[0][0], next timestep, is working: ", links[0][0].is_working)
#print("links[0][1], is working: ", links[0][1].is_working)
#links[0][1].next_timestep()
#print("links[0][1], next timestep, is working: ", links[0][1].is_working)
#print("links[1][0], is working: ", links[1][0].is_working)
#links[1][0].next_timestep()
#print("links[1][0], next timestep, is working: ", links[1][0].is_working)
#print("links[-1][0], is working: ", links[-1][0].is_working)
#links[-1][0].next_timestep()
#print("links[-1][0], next timestep, is working: ", links[-1][0].is_working)



"""Test of Class 'Chain' - Next Time Step"""
#print("Test of Class 'Chain' - Next Time Step")
#memory_numbers = [3,1,1,3,3,1,1,3]
#links = memb.create_chain_doubling(memory_numbers = memory_numbers,generation_probability=1)
#chain = memb.Chain(links)
#print("chain.links[0][0], is working: ", chain.links[0][0].is_working)
#print("chain.links[0][1], is working: ", chain.links[0][1].is_working)
#print("chain.links[0][2], is working: ", chain.links[0][2].is_working)
#print("chain.links[0][3], is working: ", chain.links[0][3].is_working)
#print("chain.links[1][0], is working: ", chain.links[1][0].is_working)
#print("chain.links[1][1], is working: ", chain.links[1][1].is_working)
#print("chain.links[2][0], is working: ", chain.links[2][0].is_working)
#print("timestep = 1")
#chain.next_timestep()
#print("chain.links[0][0], is working: ", chain.links[0][0].is_working)
#print("chain.links[0][1], is working: ", chain.links[0][1].is_working)
#print("chain.links[0][2], is working: ", chain.links[0][2].is_working)
#print("chain.links[0][3], is working: ", chain.links[0][3].is_working)
#print("chain.links[1][0], is working: ", chain.links[1][0].is_working)
#print("chain.links[1][1], is working: ", chain.links[1][1].is_working)
#print("chain.links[2][0], is working: ", chain.links[2][0].is_working)
#print("timestep = 2")
#chain.next_timestep()
#print("chain.links[0][0], is working: ", chain.links[0][0].is_working)
#print("chain.links[0][1], is working: ", chain.links[0][1].is_working)
#print("chain.links[0][2], is working: ", chain.links[0][2].is_working)
#print("chain.links[0][3], is working: ", chain.links[0][3].is_working)
#print("chain.links[1][0], is working: ", chain.links[1][0].is_working)
#print("chain.links[1][1], is working: ", chain.links[1][1].is_working)
#print("chain.links[2][0], is working: ", chain.links[2][0].is_working)
#print("timestep = 3")
#chain.next_timestep()
#print("chain.links[0][0], is working: ", chain.links[0][0].is_working)
#print("chain.links[0][1], is working: ", chain.links[0][1].is_working)
#print("chain.links[0][2], is working: ", chain.links[0][2].is_working)
#print("chain.links[0][3], is working: ", chain.links[0][3].is_working)
#print("chain.links[1][0], is working: ", chain.links[1][0].is_working)
#print("chain.links[1][1], is working: ", chain.links[1][1].is_working)
#print("chain.links[2][0], is working: ", chain.links[2][0].is_working)



"""Test of Class 'Chain' - Waiting Times"""
print("Test of Class 'Chain' - Waiting Times")
#memory_numbers = [3,1,1,3,3,1,1,3]
#generation_probability=0.5
#links = memb.create_chain_doubling(memory_numbers = memory_numbers,generation_probability=generation_probability)
#chain = memb.Chain(links)
#chain.find_waiting_time()
#print("waiting time: ", chain.waiting_time)
#n = 4
#q = 1 - generation_probability
#expval = sum([(-1)**(j + 1)*scipy.special.binom(n,j)/(1-q**j) for j in range (1,n)])
#print("expval: ", expval)

"""Test of statistics"""
print("Test of statistics")
memory_numbers = [1,1,1,1,1,1,1,1]
generation_probability=0.2
swapping_probability=1
number_of_repetitions=1000
e = memb.get_statistics(memory_numbers = memory_numbers,generation_probability=generation_probability, number_of_repetitions=number_of_repetitions,swapping_probability=swapping_probability)


n = 4
q = 1 - generation_probability
expval = sum([(-1)**(j + 1)*scipy.special.binom(n,j)/(1-q**j) for j in range (1,n+1)])
print("computed expectation value: ", expval)








