package ch.ffhs.search.api;

import ch.ffhs.search.SearchService;
import ch.ffhs.search.model.Song;
import ch.ffhs.search.repository.SongRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

import java.util.Optional;

@Controller
@CrossOrigin(origins = "http://localhost:3000")
@RequestMapping(path="/search")
public class SearchApi {
    @Autowired
    private SongRepository songRepository;

    @Autowired
    private SearchService searchService;

    @GetMapping(path="/idTest")
    public @ResponseBody
    void getSongById() {
        Optional<Song> result = songRepository.findById("5f33e258-378c-4180-866c-11c1c450d79b");


        System.out.print("DONE");
    }

    @GetMapping(path="/lyricsTest")
    public @ResponseBody
    void searchInLyrics() {
        Page<Song> result = songRepository.findByCustomQuery("murder", PageRequest.of(0,10));


        System.out.print("DONE");
    }
    @GetMapping(path="/all")
    public @ResponseBody
    Page<Song> getAll() {
        Page<Song> result = songRepository.findAll(PageRequest.of(0, 10));


        System.out.print("DONE");
        return result;
    }

    // New code here, above is for reference since it worked once
    @GetMapping(path="/search")
    public @ResponseBody Page<Song> search(@RequestParam String searchTerm,
                                           @RequestParam String artistTerm,
                                           @RequestParam boolean artistIsAnd,
                                           @RequestParam String genreTerm,
                                           @RequestParam boolean genreIsAnd){
        Page<Song> result = searchService.search(searchTerm, artistTerm, artistIsAnd, genreTerm, genreIsAnd);
        System.out.print("Breakpoint print");
        return result;
    }
}
