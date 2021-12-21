import {observable} from "mobx";
import {ISongData} from "../../util/apiTypings";


export default class Song{
    @observable id:string = "";
    @observable artist:string = "";
    @observable song:string = "";
    @observable lyrics:string = "";
    @observable genre:string = "";
    @observable language:string = "";

    /*constructor(id:string, artist:string, song:string, lyrics:string, genre:string, language:string){
        this.id = id;
        this.artist = artist;
        this.song = song;
        this.lyrics = lyrics;
        this.genre = genre;
        this.language = language;
    }*/

    public static createFromISongData(dto:ISongData){
        const song = new Song();
        song.id = dto.id;
        song.artist = dto.artist;
        song.song = dto.song;
        song.lyrics = dto.lyrics;
        song.genre = dto.genre;
        song.language = dto.language;

        return song;
    }
}