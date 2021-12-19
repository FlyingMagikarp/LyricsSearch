import {action, observable} from "mobx";
import RootStore from "../../rootStore";
import Song from "../model/song";


export default class DataStore {
    public static storeName: string = 'leagueStore';

    public rootStore: RootStore;

    @observable isLoading: boolean = false;
    @observable searchTerm: string = "";
    @observable artistTerm: string = "";
    @observable genreTerm: string = "";
    @observable artistIsAnd: boolean = true;
    @observable genreIsAnd: boolean = true;

    @observable songs: Song[] = [];
    @observable currentSong: Song = new Song("","","","","","");



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


}