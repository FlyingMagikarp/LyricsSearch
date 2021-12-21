package ch.ffhs.search.model;

import org.springframework.data.annotation.Id;
import org.springframework.data.solr.core.mapping.Indexed;
import org.springframework.data.solr.core.mapping.SolrDocument;

@SolrDocument(solrCoreName = "mll")
public class Song {

    @Id
    @Indexed(name = "id", type = "string")
    private String id;

    @Indexed(name = "artist", type = "string")
    private String artist;

    @Indexed(name = "song", type = "string")
    private String song;

    @Indexed(name = "lyrics", type = "string")
    private String lyrics;

    @Indexed(name = "genre", type = "string")
    private String genre;

    @Indexed(name = "language", type = "string")
    private String language;

    public SongDto getDto(){
        SongDto dto = new SongDto();
        dto.id = this.id;
        dto.artist = this.artist;
        dto.song = this.song;
        dto.lyrics = this.lyrics;
        dto.genre = this.genre;
        dto.language = this.language;

        return dto;
    }
}
