<h2>Simple Programming</h2>

<h4>Problem Statement:</h4>
<p>Can you help me? I need to know how many lines there are where the number of 0's is a multiple of 3 or the numbers of 1s is a multiple of 2. Please! Here is the file: <a href="https://mega.nz/#!7aoVEKhK!BAohJ0tfnP7bISIkbADK3qe1yNEkzjHXLKoJoKmqLys">https://mega.nz/#!7aoVEKhK!BAohJ0tfnP7bISIkbADK3qe1yNEkzjHXLKoJoKmqLys</a></p>

<h4>Step-1:</h4>
<p>Download the file <code>data.dat</code> from the given Cloud URL.</p>

<h4>Step-2:</h4>
<p>Create a python script file using the code given below:</p>
<pre>
<pre><span class="pl-s1">count</span> <span class="pl-c1">=</span> <span class="pl-c1">0</span>

<span class="pl-s1">file</span> <span class="pl-c1">=</span> <span class="pl-s">'data.dat'</span>

<span class="pl-k">with</span> <span class="pl-en">open</span>(<span class="pl-s1">file</span>) <span class="pl-k">as</span> <span class="pl-s1">f</span>:    
        <span class="pl-s1">l</span> <span class="pl-c1">=</span> <span class="pl-s1">f</span>.<span class="pl-en">readlines</span>()
        <span class="pl-k">for</span> <span class="pl-s1">line</span> <span class="pl-c1">in</span> <span class="pl-s1">l</span>:
                <span class="pl-s1">zero</span> <span class="pl-c1">=</span> <span class="pl-s1">line</span>.<span class="pl-en">count</span>(<span class="pl-s">'0'</span>)
                <span class="pl-s1">one</span> <span class="pl-c1">=</span> <span class="pl-s1">line</span>.<span class="pl-en">count</span>(<span class="pl-s">'1'</span>)
                <span class="pl-k">if</span> (<span class="pl-s1">zero</span><span class="pl-c1">%</span><span class="pl-c1">3</span> <span class="pl-c1">==</span> <span class="pl-c1">0</span>) <span class="pl-c1">or</span> (<span class="pl-s1">one</span><span class="pl-c1">%</span><span class="pl-c1">2</span> <span class="pl-c1">==</span> <span class="pl-c1">0</span>):
                        <span class="pl-s1">count</span> <span class="pl-c1">=</span> <span class="pl-s1">count</span> <span class="pl-c1">+</span> <span class="pl-c1">1</span>

<span class="pl-en">print</span>(<span class="pl-s">"Number of lines: "</span> <span class="pl-c1">+</span> <span class="pl-en">str</span>(<span class="pl-s1">count</span>))
<span class="pl-s1">f</span>.<span class="pl-en">close</span>()</pre>
</pre>

<h4>Step-3:</h4>
<p>Execute the above file using the command <code>python3 getFlag.py</code>. The output will give you the flag.

<h4>Step-4:</h4>
<p>We get the desired flag as <code>CTFlearn{6662}</code></p>
