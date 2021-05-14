<h2>Taking LS</h2>

<h4>Problem Statement:</h4>
<p>Just take the Ls. Check out this zip file and I be the flag will remain hidden. <a href"https://mega.nz/#!mCgBjZgB!_FtmAm8s_mpsHr7KWv8GYUzhbThNn0I8cHMBi4fJQp8">https://mega.nz/#!mCgBjZgB!_FtmAm8s_mpsHr7KWv8GYUzhbThNn0I8cHMBi4fJQp8</a></p>
  
<h4>Step-1:</h4>
<p>Download the given zip <code>The Flag.zip</code> from the cloud. Unzip the folder. You will find 2 directories <code>__MACOSX</code> & <code>The Flag</code>.</p>

<h4>Step-2:</h4>
<p>Navigate to the subfolder <code>The Flag</code> using the terminal and execute the command <code>ls -la</code>. You will get a similar output as given below:</p>
<pre>
total 32
drwxr-xr-x 1 atharva 197121     0 May 15 00:07  ./
drwxr-xr-x 1 atharva 197121     0 May 15 00:07  ../
-rw-r--r-- 1 atharva 197121  6148 May 15 00:07  .DS_Store
drwxr-xr-x 1 atharva 197121     0 May 15 00:07  .ThePassword/
-rw-r--r-- 1 atharva 197121 16647 May 15 00:07 'The Flag.pdf'
</pre>
<p>We find that the file <code>The Flag.pdf</code> is password protected.</p>

<h4>Step-3:</h4>
<p>Now navigate to the subfolder <code>.ThePassword</code> using the terminal and execute the command <code>ls -la</code>. You will get a similar output as given below:</p>
<pre>
total 5
drwxr-xr-x 1 atharva 197121  0 May 15 00:07 ./
drwxr-xr-x 1 atharva 197121  0 May 15 00:07 ../
-rw-r--r-- 1 atharva 197121 42 May 15 00:07 ThePassword.txt
</pre>

<h4>Step-4:</h4>
Acquire the password from the file ThePassword.txt using the command <code>cat ThePassword.txt</code>. The text found inside this file is <code>Nice Job!  The Password is "Im The Flag".</code></p>

<h4>Step-5:</h4>
<p>Input the password <code>Im The Flag</code> to open the file <code>The Flag.pdf</code>.
  
<h4>Step-6:</h4>
<p>The desired flag inside the pdf is <code>ABCTF{T3Rm1n4l_is_C00l}</code></p>
