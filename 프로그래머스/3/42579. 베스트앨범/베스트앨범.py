def solution(genres, plays):
    genre_total = {}
    song_by_genre = {}
    
    for i in range(len(genres)):
        g, p = genres[i], plays[i]
        genre_total[g] = genre_total.get(g, 0) + p
        
        if g not in song_by_genre:
            song_by_genre[g] = []
        song_by_genre[g].append((p, i))
        
    sorted_genre = sorted(genre_total.items(), key = lambda x : x[1], reverse = True)
    
    answer = []
    for g, _ in sorted_genre:
        song_by_genre[g].sort(key=lambda x:(-x[0], x[1]))
        
        answer.extend([i for _, i in song_by_genre[g][:2]])
    return answer