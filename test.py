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
#elemlink = memb.Elementary_Link(memoryL=memb.Memory(buffer_space=5),generation_probability=1)
#print("working? ", elemlink.is_working)
#print("free memory space, L: ", elemlink.memoryL.buffer_space - elemlink.memoryL.occupied_buffer_space, "R: ", elemlink.memoryR.buffer_space - elemlink.memoryR.occupied_buffer_space)
#elemlink.check_buffer_space()
#print("ready for generatin? ", elemlink.ready_for_generation)
#elemlink.generation_attempt()
#print("generation successful? ", elemlink.is_working)
#print("free memory space, L: ", elemlink.memoryL.buffer_space - elemlink.memoryL.occupied_buffer_space, "R: ", elemlink.memoryR.buffer_space - elemlink.memoryR.occupied_buffer_space)
#elemlink.check_buffer_space()
#print("ready for generatin? ", elemlink.ready_for_generation)
#elemlink.turn_off()
#print("free memory space, L: ", elemlink.memoryL.buffer_space - elemlink.memoryL.occupied_buffer_space, "R: ", elemlink.memoryR.buffer_space - elemlink.memoryR.occupied_buffer_space)
#elemlink.turn_off()



####Hier tauchen Fehler auf!####
"""Test of Long Link"""
print("Test of Long Link")
link1 = memb.Elementary_Link()
link2 = memb.Elementary_Link()
llink = memb.Long_Link(link1=link1,link2=link2)
llink.check_swapping_conditions()
print("ready for swapping? ", llink.ready_for_swapping)
llink.link1.generation_attempt()
llink.link2.generation_attempt()
llink.check_swapping_conditions()
print("ready for swapping? ", llink.ready_for_swapping)
llink.swapping_attempt()
