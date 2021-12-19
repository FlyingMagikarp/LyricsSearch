package ch.ffhs.search.repository;

import ch.ffhs.search.model.Song;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.solr.repository.Query;
import org.springframework.data.solr.repository.SolrCrudRepository;

import java.util.Optional;

public interface SongRepository extends SolrCrudRepository<Song, String> {

    public Optional<Song> findById(String id);

    @Query("id:*?0*")
    public Page<Song> findByNamedQuery(String searchTerm, Pageable pageable);

    @Query("lyrics:*?0*")
    public Page<Song> findByCustomQuery(String searchTerm, Pageable pageable);

    @Query("*:*")
    public Page<Song> findAll(Pageable pageable);

    @Query("lyrics*?0*")
    public Page<Song> findSongByLyrics(String searchTerm, Pageable pageable);

    @Query("lyrics:*?0* AND artist:*?1*")
    public Page<Song> findSongByLyricsAndArtist(String searchTerm, String artistTerm, Pageable pageable);

    @Query("lyrics:*?0* NOT artist:*?1*")
    public Page<Song> findSongByLyricsAndArtistNot(String searchTerm, String artistTerm, Pageable pageable);

    @Query("lyrics:*?0* AND genre:*?1*")
    public Page<Song> findSongByLyricsAndGenre(String searchTerm, String genreTerm, Pageable pageable);

    @Query("lyrics:*?0* NOT genre:*?1*")
    public Page<Song> findSongByLyricsAndGenreNot(String searchTerm, String genreTerm, Pageable pageable);

    @Query("lyrics:*?0* AND artist:*?1* AND genre:*?2*")
    public Page<Song> findSongByLyricsAndArtistAndGenre(String searchTerm, String artistTerm, String genreTerm, Pageable pageable);

    @Query("lyrics:*?0* NOT artist:*?1* NOT genre:*?2*")
    public Page<Song> findSongByArtistAndArtistNotAndGenreNot(String searchTerm, String artistTerm, String genreTerm, Pageable pageable);

    @Query("lyrics:*?0* AND artist:*?1* NOT genre:*?2*")
    public Page<Song> findSongByLyricsAndArtistAndGenreNot(String searchTerm, String artistTerm, String genreTerm, Pageable pageable);

    @Query("lyrics:*?0* AND genre:*?1* NOT artist:*?2*")
    public Page<Song> findSongByLyricsAndGenreAndArtistNot(String searchTerm, String genreTerm, String artistTerm, Pageable pageable);
}
