import subprocess

# # Example command to list files in the current directory
# command = "git pull origin main"

# # Execute the command
# process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# # Wait for the command to complete and capture the output
# stdout, stderr = process.communicate()

# # Decode the byte strings to UTF-8 and print the output
# if stdout:
#     print(stdout.decode('utf-8'))
# if stderr:
#     print(stderr.decode('utf-8'))

# exec(open('./Run_Check.py').read())
# exec(open('./zentao_noctool_kaidan.py').read())
# exec(open('./aliyun.py').read())
# exec(open('./tencent.py').read())
# exec(open('./huawei.py').read())
# exec(open('./ucloud.py').read())
# exec(open('./gname_juming_7211_com.py').read())
# exec(open('./zentaowater.py').read())
# exec(open('./noctoolwater.py').read())
# exec(open('./zentao_noctool_zanting.py').read()) 

subprocess.run(["python3", "./Run_Check.py"])
subprocess.run(["python3", "./zentao_noctool_kaidan.py"])
subprocess.run(["python3", "./aliyun.py"])
subprocess.run(["python3", "./tencent.py"])
subprocess.run(["python3", "./huawei.py"])
subprocess.run(["python3", "./ucloud.py"])
subprocess.run(["python3", "./gname_juming_7211_com.py"])
subprocess.run(["python3", "./zentaowater.py"])
subprocess.run(["python3", "./noctoolwater.py"])
subprocess.run(["python3", "./zentao_noctool_zanting.py"])