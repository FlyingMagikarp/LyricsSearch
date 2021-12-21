package ch.ffhs.search;

import org.apache.solr.client.solrj.SolrClient;
import org.apache.solr.client.solrj.impl.HttpSolrClient;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;
import org.springframework.data.solr.core.SolrTemplate;
import org.springframework.data.solr.repository.config.EnableSolrRepositories;

@Configuration
@EnableSolrRepositories(
        basePackages = "ch.ffhs.search.repository")
@ComponentScan
public class SolrConfig {

    @Bean
    public SolrClient solrClient() {
        //return new HttpSolrClient.Builder("http://86.119.30.88:8983//solr").build();
        return new HttpSolrClient.Builder("http://localhost:8983//solr").build();
    }

    @Bean
    public SolrTemplate solrTemplate(SolrClient client) throws Exception {
        return new SolrTemplate(client);
    }
}
