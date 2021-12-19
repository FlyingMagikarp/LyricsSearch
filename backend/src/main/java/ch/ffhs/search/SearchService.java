package ch.ffhs.search;

import ch.ffhs.search.model.Song;
import ch.ffhs.search.repository.SongRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.stereotype.Service;

@Service
public class SearchService {
    @Autowired
    private SongRepository songRepository;

    public Page<Song> search(String searchTerm, String artistTerm, boolean artistIsAnd, String genreTerm, boolean genreIsAnd){
        if(searchTerm.equals("")){
            return songRepository.findAll(PageRequest.of(0, 10));
        } else if (artistIsAnd && genreIsAnd){
            return songRepository.findSongByLyricsAndArtistAndGenre(searchTerm, artistTerm, genreTerm, PageRequest.of(0, 10));
        } else if (!artistIsAnd && !genreIsAnd){
            return songRepository.findSongByArtistAndArtistNotAndGenreNot(searchTerm, artistTerm, genreTerm, PageRequest.of(0, 10));
        } else if (artistIsAnd){
            return songRepository.findSongByLyricsAndArtistAndGenreNot(searchTerm, artistTerm, genreTerm, PageRequest.of(0, 10));
        } else {
            return songRepository.findSongByLyricsAndGenreAndArtistNot(searchTerm, genreTerm, artistTerm, PageRequest.of(0, 10));
        }
    }
}
