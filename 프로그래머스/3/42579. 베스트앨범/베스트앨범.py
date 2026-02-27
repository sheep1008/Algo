def solution(genres, plays):
    genre_total = {}
    songs_by_genre= {}
    
    for i in range(len(genres)):
        g, p = genres[i], plays[i]
        genre_total[g] = genre_total.get(g, 0) + p
        if g not in songs_by_genre:
            songs_by_genre[g] = []
        songs_by_genre[g].append((p, i))
        
    sorted_genres = sorted(genre_total.items(), key=lambda x: x[1], reverse=True)
    
    answer = []
    for g, _ in sorted_genres:
        songs_by_genre[g].sort(key=lambda x: (-x[0], x[1]))
        
        answer.extend([idx for p, idx in songs_by_genre[g][:2]])
        
    return answer