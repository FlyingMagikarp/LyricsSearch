docker rm -f mll_solr
docker build -t mll_solr .
docker run -d -p 8983:8983 --name mll_solr mll_solr

sleep 15
cd ../../data
python3 send_to_solr.py