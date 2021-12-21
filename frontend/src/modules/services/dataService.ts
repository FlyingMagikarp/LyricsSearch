import Constants from "../../util/Constants";
import axios from "axios";


const DataService = {
    async performSearch(searchTerm:string, artistTerm:string, artistIsAnd:boolean, genreTerm:string, genreIsAnd:boolean): Promise<any> {
        const result = await axios.get(Constants.C_API_BASEURL + 'search/search', {
            params: {   searchTerm: searchTerm,
                        artistTerm: artistTerm,
                        artistIsAnd: artistIsAnd,
                        genreTerm: genreTerm,
                        genreIsAnd: genreIsAnd}});
        return result.data
    }
};

export default DataService;