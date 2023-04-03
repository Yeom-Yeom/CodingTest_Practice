def clear_wallpaper(wallpaper):
    a,b = [],[]
    for x in range(len(wallpaper)):
        for y in range(len(wallpaper[x])):
            if wallpaper[x][y] == '#':
                a.append(x)
                b.append(y)
    return [min(a),min(b),max(a)+1, max(b)+1]

clear_wallpaper([".#...", "..#..", "...#."])
        
