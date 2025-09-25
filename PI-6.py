from commons import extrairMatrizCinza
import numpy as np
import matplotlib.pyplot as plt
import argparse
import csv
import os
import cv2


def build_histogram(img, L=256):
	lin, col = img.shape
	hist = [0] * L
	for i in range(lin):
		row = img[i]
		for j in range(col):
			pix = int(row[j])
			hist[pix] += 1
	return hist


def normalize_hist(hist, n_total):
	return [h / n_total for h in hist]


def cdf_from_prob(prob):
	L = len(prob)
	cdf = [0.0] * L
	cdf[0] = prob[0]
	for k in range(1, L):
		cdf[k] = cdf[k-1] + prob[k]
	return cdf


def build_lut(cdf, L=256):
	return [round(c * (L - 1)) for c in cdf]


def apply_lut(img, lut):
	lin, col = img.shape
	out = np.zeros_like(img, dtype=np.uint8)
	for i in range(lin):
		row = img[i]
		for j in range(col):
			out[i, j] = lut[int(row[j])]
	return out


def save_hist_plot(hist, filename, title="Histograma"):
	plt.figure(figsize=(8,4))
	plt.bar(range(len(hist)), hist, width=1.0, color='gray')
	plt.title(title)
	plt.xlabel('Nível de cinza')
	plt.ylabel('Número de pixels')
	plt.tight_layout()
	plt.savefig(filename)
	plt.close()


def save_prob_plot(prob, filename, title="Distribuição (pr)"):
	plt.figure(figsize=(8,4))
	plt.plot(range(len(prob)), prob, color='blue')
	plt.title(title)
	plt.xlabel('Nível de cinza')
	plt.ylabel('Probabilidade')
	plt.tight_layout()
	plt.savefig(filename)
	plt.close()


def write_table_csv(hist, prob, cdf, lut, filename):
	with open(filename, 'w', newline='') as csvfile:
		writer = csv.writer(csvfile)
		writer.writerow(['rk', 'nk', 'pr(rk)', 'CDF', 'Eq(rk)'])
		for k in range(len(hist)):
			writer.writerow([k, hist[k], f"{prob[k]:.6f}", f"{cdf[k]:.6f}", lut[k]])


def ensure_dir(path):
	os.makedirs(path, exist_ok=True)


def main():
	parser = argparse.ArgumentParser(description='Equalização de histograma - implementação manual')
	parser.add_argument('--input', '-i', required=False, help='Caminho da imagem (escala de cinza). Se ausente, usa extrairMatrizCinza() do commons')
	parser.add_argument('--output_dir', '-o', default='out_equalization', help='Pasta de saída')
	args = parser.parse_args()

	out_dir = args.output_dir
	ensure_dir(out_dir)

    # 1) Carregar imagem
	img = extrairMatrizCinza()

	lin, col = img.shape
	n_total = lin * col

	# 2) Construir histograma nk
	L = 256
	hist = build_histogram(img, L=L)

	# 3) Normalizar histograma
	prob = normalize_hist(hist, n_total)

	# 4) CDF acumulada
	cdf = cdf_from_prob(prob)

	# 5) LUT
	lut = build_lut(cdf, L=L)

	# 6) Transformar a imagem
	img_eq = apply_lut(img, lut)

	# 7) Salvar resultados
	original_img_path = os.path.join(out_dir, 'original.png')
	equalized_img_path = os.path.join(out_dir, 'equalized.png')
	cv2.imwrite(original_img_path, img)
	cv2.imwrite(equalized_img_path, img_eq)

	# Histogramas
	save_hist_plot(hist, os.path.join(out_dir, 'hist_original.png'), title='Histograma - Original (nk)')
	hist_eq = build_histogram(img_eq, L=L)
	save_hist_plot(hist_eq, os.path.join(out_dir, 'hist_equalized.png'), title='Histograma - Equalizada (nk)')

	# Probabilidade e CDF
	save_prob_plot(prob, os.path.join(out_dir, 'prob_original.png'), title='Distribuição pr(rk) - Original')
	save_prob_plot(cdf, os.path.join(out_dir, 'cdf.png'), title='CDF (acumulada)')

	# Tabela didática
	table_csv = os.path.join(out_dir, 'table_rk_nk_pr_cdf_eq.csv')
	write_table_csv(hist, prob, cdf, lut, table_csv)

	print('Equalização manual concluída.')
	print(f'Arquivos salvos em: {out_dir}')


if __name__ == '__main__':
	main()


