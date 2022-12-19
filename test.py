import memory_buffer_doubling as memb


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




"""Test of Long Link"""
#print("Test of Long Link")
#link1 = memb.Elementary_Link(memoryL = memb.Memory(),memoryR = memb.Memory())
#link2 = memb.Elementary_Link(memoryL = memb.Memory(),memoryR = memb.Memory())
#llink = memb.Long_Link(link1=link1,link2=link2,swapping_probability=0.7)
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
#llink.swapping_attempt()
#print("swapping attempt, is working: ", llink.is_working)
#print("free memory space, L: ", llink.memoryL.buffer_space - llink.memoryL.occupied_buffer_space, "R: ", llink.memoryR.buffer_space - llink.memoryR.occupied_buffer_space)
#llink.turn_off()
#print("turn off, is working: ", llink.is_working)
#print("free memory space, L: ", llink.memoryL.buffer_space - llink.memoryL.occupied_buffer_space, "R: ", llink.memoryR.buffer_space - llink.memoryR.occupied_buffer_space)


"""Test of Chain Generation"""
print("Test of Chain Generation - each step")
memory_numbers = [3,1,1,3,3,1,1,3]
linklist = memb.create_elementary_links(memory_numbers=memory_numbers)
print("length of elementary linklist: ", len(linklist))
linklist = memb.create_long_links_doubling(linklist, swapping_probability=1)
print("length of longer linklist: ", len(linklist))
linklist = memb.create_long_links_doubling(linklist, swapping_probability=1)
print("length of longer linklist: ", len(linklist))
print("Test of Chain Generation - combine")
links = memb.create_chain_doubling()
print("steps: ", len(links))
print("length of elementary linklist: ", len(links[0]))
print("length of longer linklist: ", len(links[1]))
print("length of longer linklist: ", len(links[2]))

