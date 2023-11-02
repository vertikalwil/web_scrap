kec=(
 'Panongan'
)

for x in "${kec[@]}"; do
    /home/vertikal/.local/bin/scrapy crawl housescrap -o ~/data_science/airflow_docker/data_csv/tangerang.csv -a start_url="https://www.rumah123.com/jual/tangerang/$x/rumah/"
done













kec2=(
 'BSD Delatinos' 
 'Serua' 
 'Karawaci' 
 'Jombang'
 'Cikupa' 
 'Curug' 
 'Suradita' 
 'Panongan' 
 'BSD Residence One'
 'Kelapa Dua' 
 'Pondok Ranji' 
 'Ciledug' 
 'Pondok Cabe'
 'Gading Serpong' 
 'Pagedangan' 
 'Legok' 
 'Pinang' 
 'Cikokol'
 'Dadap' 
 'BSD Foresta' 
 'BSD Green Wich' 
 'Cireundeu'
 'BSD Anggrek Loka' 
 'Cipondoh' 
 'BSD Nusaloka' 
 'BSD Puspita Loka'
 'Gading Serpong Pondok Hijau Golf' 
 'BSD The Green' 
 'Cipadu'
 'Larangan' 
 'BSD Giri Loka' 
 'Cikupa Citra Raya' 
 'Modernland'
 'Benda' 
 'Rempoa' 
 'Alam Sutera' 
 'BSD' 
 'Cisauk' 
 'Graha Raya'
 'Lippo Karawaci'
)