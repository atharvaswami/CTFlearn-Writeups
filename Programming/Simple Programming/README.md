<h2>Simple Programming</h2>

<h4>Problem Statement:</h4>
<p>Can you help me? I need to know how many lines there are where the number of 0's is a multiple of 3 or the numbers of 1s is a multiple of 2. Please! Here is the file: <a href="https://mega.nz/#!7aoVEKhK!BAohJ0tfnP7bISIkbADK3qe1yNEkzjHXLKoJoKmqLys">https://mega.nz/#!7aoVEKhK!BAohJ0tfnP7bISIkbADK3qe1yNEkzjHXLKoJoKmqLys</a></p>

<h4>Step-1:</h4>
<p>Download the file <code>data.dat</code> from the given Cloud URL.</p>

<h4>Step-2:</h4>
<p>Create a python script file using the code given below:</p>
<pre>
flag=0
with open('data.dat') as F:
    L = F.readlines()  
    for S in L:
        try:
            if(S.count('0')%3==0 or S.count('1')%2==0):
                flag+=1
        except EOFError:
            break
print("CTFlearn{" + str(flag) + "}")
F.close()
</pre>

<h4>Step-3:</h4>
<p>Execute the above file using the command <code>python3 getFlag.py</code>. The output will give you the flag.

<h4>Step-4:</h4>
<p>We get the desired flag as <code>CTFlearn{6662}</code></p>
