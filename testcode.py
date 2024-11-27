import asyncio

async def tugas_siram_tanaman():
    print("Mulai menyiram tanaman...")
    await asyncio.sleep(3)  # Menunggu selama 3 detik, tetapi kode lain masih bisa berjalan
    print("Selesai menyiram tanaman!")

async def tugas_memasak_air():
    print("Mulai memasak air...")
    await asyncio.sleep(5)  # Menunggu selama 5 detik
    print("Selesai memasak air!")

# Fungsi utama untuk menjalankan tugas-tugas tersebut secara bersamaan
async def main():
    # Menjalankan kedua tugas secara bersamaan
    await asyncio.gather(tugas_siram_tanaman(), tugas_memasak_air())

# Menjalankan semua tugas
asyncio.run(main())
