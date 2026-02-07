from __future__ import annotations

import numpy as np


def reproducibility_example():
	print("--- reproducibility_example ---")
	rng1 = np.random.default_rng(42)
	rng2 = np.random.default_rng(42)

	a = rng1.integers(0, 100, size=5)
	b = rng2.integers(0, 100, size=5)
	print("rng1 integers:", a)
	print("rng2 integers (same seed):", b)
	print("equal:", np.array_equal(a, b))


def integers_and_choice():
	print("--- integers_and_choice ---")
	rng = np.random.default_rng()
	# random integers in [low, high)
	ints = rng.integers(0, 10, size=6)
	print("random integers:", ints)

	# choice with and without replacement
	items = np.array(["red", "green", "blue"])
	picks_replace = rng.choice(items, size=5, replace=True)
	picks_noreplace = rng.choice(items, size=3, replace=False)
	print("choice with replace:", picks_replace)
	print("choice without replace:", picks_noreplace)

	# weighted probabilities
	probs = [0.7, 0.2, 0.1]
	weighted = rng.choice(items, size=10, p=probs)
	print("weighted choice:", weighted)


def permutation_and_shuffle():
	print("--- permutation_and_shuffle ---")
	rng = np.random.default_rng(1)
	arr = np.arange(10)
	perm = rng.permutation(arr)
	print("original:", arr)
	print("permutation (returns new array):", perm)

	# shuffle modifies in-place
	arr2 = arr.copy()
	rng.shuffle(arr2)
	print("shuffled in-place:", arr2)


def distributions_examples():
	print("--- distributions_examples ---")
	rng = np.random.default_rng(0)

	# uniform on [0, 1)
	u = rng.random(size=5)
	print("uniform [0,1):", u)

	# normal (Gaussian)
	normal = rng.normal(loc=0.0, scale=1.0, size=(2, 4))
	print("normal samples:\n", normal)

	# binomial (n trials, p probability)
	bino = rng.binomial(n=10, p=0.3, size=10)
	print("binomial (n=10, p=0.3):", bino)

	# multinomial (single draw of counts for k categories)
	m = rng.multinomial(n=10, pvals=[0.2, 0.5, 0.3])
	print("multinomial (n=10, pvals=[0.2,0.5,0.3]):", m)


def multivariate_and_matrix_samples():
	print("--- multivariate_and_matrix_samples ---")
	rng = np.random.default_rng(123)

	# multivariate normal via cov matrix sampling example
	mean = np.array([0.0, 1.0])
	cov = np.array([[1.0, 0.5], [0.5, 2.0]])
	samples = rng.multivariate_normal(mean, cov, size=5)
	print("multivariate normal samples:\n", samples)

	# sampling rows from a 2D dataset
	data = np.arange(20).reshape(10, 2)
	idx = rng.choice(len(data), size=4, replace=False)
	print("data:\n", data)
	print("random row indices:", idx)
	print("sampled rows:\n", data[idx])


def reproducibility_with_state():
	print("--- reproducibility_with_state ---")
	rng = np.random.default_rng(2026)
	# Capture state (bit generator state)
	state = rng.bit_generator.state
	samples1 = rng.integers(0, 100, size=4)
	print("first samples:", samples1)

	# restore and draw again to get the same samples
	rng.bit_generator.state = state
	samples2 = rng.integers(0, 100, size=4)
	print("restored samples (should match first):", samples2)
	print("equal:", np.array_equal(samples1, samples2))


def main():
	reproducibility_example()
	integers_and_choice()
	permutation_and_shuffle()
	distributions_examples()
	multivariate_and_matrix_samples()
	reproducibility_with_state()


if __name__ == "__main__":
	main()

