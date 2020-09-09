SELECT 
	produk_id,
	'produk' AS produk_type,
	NAME,
	kategori
FROM produk
UNION all
SELECT
	produk_id,
	'virtual_produk' AS produk_type,
	NAME,
	kategori
FROM virtual_produk