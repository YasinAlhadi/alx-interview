# 0x08. Making Change
<h3 class="panel-title">
      0. Change comes from within
</h3>

<p>Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount <code>total</code>.</p>

<ul>
<li>Prototype: <code>def makeChange(coins, total)</code></li>
<li>Return: fewest number of coins needed to meet <code>total</code>

<ul>
<li>If <code>total</code> is <code>0</code> or less, return <code>0</code></li>
<li>If <code>total</code> cannot be met by any number of coins you have, return <code>-1</code></li>
</ul></li>
<li><code>coins</code> is a list of the values of the coins in your possession</li>
<li>The value of a coin will always be an integer greater than <code>0</code></li>
<li>You can assume you have an infinite number of each denomination of coin in the list</li>
<li>Your solution’s runtime will be evaluated in this task</li>
</ul>

<pre><code>carrie@ubuntu:~/0x08-making_change$ cat 0-main.py
#!/usr/bin/python3
"""
Main file for testing
"""

makeChange = __import__('0-making_change').makeChange

print(makeChange([1, 2, 25], 37))

print(makeChange([1256, 54, 48, 16, 102], 1453))

carrie@ubuntu:~/0x08-making_change$
</code></pre>