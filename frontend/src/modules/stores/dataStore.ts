import {action, observable} from "mobx";
import RootStore from "../../rootStore";
import Song from "../model/song";
import DataService from "../services/dataService";
import {ISongData} from "../../util/apiTypings";


export default class DataStore {
    public static storeName: string = 'leagueStore';

    public rootStore: RootStore;

    @observable isLoading: boolean = false;
    @observable searchTerm: string = "";
    @observable artistTerm: string = "";
    @observable genreTerm: string = "Any";
    @observable artistIsAnd: boolean = true;
    @observable genreIsAnd: boolean = true;

    @observable genres: string[] = [];

    @observable songDtoList: ISongData[] = [];
    @observable songs: Song[] = [];
    @observable currentSong: Song = new Song();



    constructor(rootStore: RootStore) {
        this.rootStore = rootStore;
    }

    @action
    public updateSearchTerms(searchTerm:string, artistTerm:string, genreTerm:string, artistIsAnd:boolean, genreIsAnd:boolean){
        this.searchTerm = searchTerm;
        this.artistTerm = artistTerm;
        this.genreTerm = genreTerm;
        this.artistIsAnd = artistIsAnd;
        this.genreIsAnd = genreIsAnd;
    }

    @action
    public toggleArtistIsAnd(){
        this.artistIsAnd = !this.artistIsAnd;
    }

    @action
    public toggleGenreIsAnd(){
        this.genreIsAnd = !this.genreIsAnd;
    }

    @action
    public updateSearchTerm(searchTerm:string){
        this.searchTerm = searchTerm;
    }

    @action
    public updateArtistTerm(artistTerm:string){
        this.artistTerm = artistTerm;
    }

    @action
    public updateGenreTerm(genreTerm:string){
        this.genreTerm = genreTerm;
    }

    @action
    public async performSearch(){
        this.isLoading = true;

        await DataService.performSearch(this.searchTerm, this.artistTerm, this.artistIsAnd, this.genreTerm, this.genreIsAnd)
            .then((result) => {
                this.songDtoList = result;
                this.songs=[];
                result.map(r => {
                    this.songs.push(Song.createFromISongData(r))
                });
                this.isLoading = false;
            });

        return this.songs;
    }

}