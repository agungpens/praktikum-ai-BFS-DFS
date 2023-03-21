# Implementasi Graph sebagai dictionary
graph = {'A': ['B', 'C'],
         'B': ['H'],
         'C': ['D', 'E'],
         'D': ['F', 'G'],
         'E': ['I'],
         'F': ['H'],
         'G': ['I'],
         'H': ['I']}

# Implementasi algoritma BFS
def bfs(graph, start, goal):
    explored = []   # Untuk melacak node yang sudah dikunjungi
    queue = [[start]]   # Untuk melacak jalur yang masih harus dieksplorasi

    if start == goal:
        return "Anda sudah berada di tujuan!"

    while queue:
        path = queue.pop(0)  # Mengambil jalur terdepan dari antrian
        node = path[-1]      # Mengambil node terakhir dari jalur tersebut

        if node not in explored:
            neighbours = graph[node]    # Mengambil tetangga dari node yang sedang dieksplorasi

            # Menambahkan jalur baru ke antrian untuk setiap tetangga yang belum dieksplorasi
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

                # Return jalur jika sudah mencapai tujuan
                if neighbour == goal:
                    return new_path

            explored.append(node)   # Menandai node yang sudah dieksplorasi

    return "Tidak ditemukan jalur yang menghubungkan kedua node"

# Implementasi algoritma DFS
def dfs(graph, start, goal):
    explored = []   # Untuk melacak node yang sudah dikunjungi
    stack = [[start]]   # Untuk melacak jalur yang masih harus dieksplorasi

    if start == goal:
        return "Anda sudah berada di tujuan!"

    while stack:
        path = stack.pop()  # Mengambil jalur terakhir dari tumpukan
        node = path[-1]      # Mengambil node terakhir dari jalur tersebut

        if node not in explored:
            neighbours = graph[node]    # Mengambil tetangga dari node yang sedang dieksplorasi

            # Menambahkan jalur baru ke tumpukan untuk setiap tetangga yang belum dieksplorasi
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                stack.append(new_path)

                # Return jalur jika sudah mencapai tujuan
                if neighbour == goal:
                    return new_path

            explored.append(node)   # Menandai node yang sudah dieksplorasi

    return "Tidak ditemukan jalur yang menghubungkan kedua node"

# Memanggil fungsi BFS dan DFS untuk mencari jalur dari node A ke I
print("Jalur BFS dari A ke I:", bfs(graph, 'A', 'I'))
print("Jalur DFS dari A ke I:", dfs(graph, 'A', 'I'))