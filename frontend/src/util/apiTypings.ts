export interface ISongData {
    id: string,
    artist: string,
    song: string,
    lyrics: string,
    genre: string,
    language: string
}

export interface ISongsData {
    songs: ISongData[]
}