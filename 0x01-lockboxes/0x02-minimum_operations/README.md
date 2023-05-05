# 0x02. Minimum Operations
<p>In a text file, there is a single character <code>H</code>. Your text editor can execute only two operations in this file: <code>Copy All</code> and <code>Paste</code>. Given a number <code>n</code>, write a method that calculates the fewest number of operations needed to result in exactly <code>n</code> <code>H</code> characters in the file.</p>
<ul>
<li>Prototype: <code>def minOperations(n)</code></li>
<li>Returns an integer</li>
<li>If <code>n</code> is impossible to achieve, return <code>0</code></li>
</ul>
<p><strong>Example:</strong></p>
<p><code>n = 9</code></p>
<ul>
<li><code>H =&gt; Copy All =&gt; Paste =&gt; HH =&gt; Paste =&gt;HHH =&gt; Copy All =&gt; Paste =&gt; HHHHHH =&gt; Paste =&gt; HHHHHHHHH</code></li>
</ul>
<p>Number of operations: <code>6</code></p>