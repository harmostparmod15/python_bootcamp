import subprocess;

# command = "ping -c 1 8.8.8.8";
# output = subprocess.check_output(command.split());
# print(output.decode());


with open("./hosts.txt") as f:
    content = f.read().splitlines();
    for line in content:
        # print(line)
        try:
            command = f"ping -c 1 {line}";
            output = subprocess.check_output(command.split());
            print(output.decode());
            print("#"*50)
        except Exception as e:
            print(f"host {line} is down {e.args}");
