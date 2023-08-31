# 0x09. Island Perimeter
<p>Create a function <code>def island_perimeter(grid):</code> that returns the perimeter of the island described in <code>grid</code>:</p>
<ul>
<li><code>grid</code> is a list of list of integers:

<ul>
<li>0 represents water</li>
<li>1 represents land</li>
<li>Each cell is square, with a side length of 1</li>
<li>Cells are connected horizontally/vertically (not diagonally). </li>
<li><code>grid</code> is rectangular, with its width and height not exceeding 100</li>
</ul></li>
<li>The grid is completely surrounded by water</li>
<li>There is only one island (or nothing).</li>
<li>The island doesn’t have “lakes” (water inside that isn’t connected to the water surrounding the island).</li>
</ul>
<pre><code>guillaume@ubuntu:~/0x09$ cat 0-main.py
#!/usr/bin/python3
"""
0-main
"""
island_perimeter = __import__('0-island_perimeter').island_perimeter

if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))
</code></pre>