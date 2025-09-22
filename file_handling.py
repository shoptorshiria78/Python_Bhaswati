file_read = open('coding.txt', 'r')

print(file_read.read())

file_read.close()

file_write = open('coding.txt', 'w')

file_write.write("I love traveling a lot. Love sea more.")
file_write.write("I love to visit saint martin an Coral Island of Bangladesh.")

file_write.close()

file_append = open('coding.txt', 'a')

file_append.write("\n I also love to visit hill site. In Bangladesh we do have bandarban as a hill site area. Those are really beautiful.")

file_append.close()