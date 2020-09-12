#memilih semua kolom
SELECT * from produk
#memilih salah satu kolom
SELECT produk_id FROM produk

SELECT 
t.*,
ap.name AS Produk_name
FROM transaction t
JOIN(
SELECT 
	produk_id,
	'produk' AS produk_type,
	NAME
FROM produk
UNION all
SELECT
	produk_id,
	'virtual_produk' AS produk_type,
	NAME
FROM virtual_produk
) ap ON ap.produk_id = t.produk_id AND ap.produk_type = t.produk_type;