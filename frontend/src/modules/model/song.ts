import {observable} from "mobx";


export default class Song{
    @observable id:string;
    @observable artist:string;
    @observable song:string;
    @observable lyrics:string;
    @observable genre:string;
    @observable language:string;

    constructor(id:string, artist:string, song:string, lyrics:string, genre:string, language:string){
        this.id = id;
        this.artist = artist;
        this.song = song;
        this.lyrics = lyrics;
        this.genre = genre;
        this.language = language;
    }
}