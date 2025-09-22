output_file = open("new_file.txt", 'w')
input_file = open("hello.txt", 'r')

line_seen_so_far = set()

for line in input_file:
    
    if line not in line_seen_so_far:
        
        line_seen_so_far.add(line)
        output_file.write(line)
        
input_file.close()
output_file.close()