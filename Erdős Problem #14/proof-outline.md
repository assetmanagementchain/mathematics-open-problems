Erdős Problem #14
Unbounded gaps in infinite Sidon sets

🔗 https://www.erdosproblems.com/14

Theorem

Let

<img width="544" height="109" alt="image" src="https://github.com/user-attachments/assets/5e81751c-dd5e-42c4-9446-9f62dd1fddb1" />


be an infinite Sidon set.
Then

<img width="387" height="115" alt="image" src="https://github.com/user-attachments/assets/32f740b4-2ad9-4a2e-8a80-c1698ee0bc17" />


Equivalently, every infinite Sidon set contains a Sidon subset whose gaps tend to infinity.

Preliminaries

Recall that a Sidon set satisfies:

<img width="549" height="92" alt="image" src="https://github.com/user-attachments/assets/e45757b8-67fd-4b0d-9aa7-3b7b2d7606f3" />

In particular, all pairwise sums with 𝑎≤𝑏 are distinct.

Lemma 1 (Bounded gaps imply local density)

Assume there exists 𝑀>0 such that

<img width="268" height="85" alt="image" src="https://github.com/user-attachments/assets/6d92f3f0-46fc-466f-a08d-b641c9bbb195" />

for all i.

Then for any sufficiently large interval [𝑥,𝑥+𝐿] ,

<img width="432" height="114" alt="image" src="https://github.com/user-attachments/assets/9b4ffedd-ade0-41ef-aa7c-3e87f9f77b57" />

Proof

Between any two consecutive elements of 𝐴, the gap is at most 𝑀.
Thus in an interval of length 𝐿, one can fit at least ⌊𝐿/𝑀⌋ elements of 𝐴, up to boundary effects. ∎

Lemma 2 (Lower bound on number of sums)

<img width="564" height="55" alt="image" src="https://github.com/user-attachments/assets/f8e944a6-b492-4551-82a6-f5030dbdede3" />

Then the set of sums

<img width="622" height="95" alt="image" src="https://github.com/user-attachments/assets/5d39f4f3-a80a-4b72-a337-8c2800069399" />


contains exactly 
<img width="98" height="80" alt="image" src="https://github.com/user-attachments/assets/4f0596de-3b28-46db-af0d-679308ebd393" />
​ distinct elements.

Proof

This is immediate from the Sidon property, which guarantees all pairwise sums are distinct. ∎

Lemma 3 (Upper bound on possible sums)

All sums in 𝑆+𝑆
S+S lie in the interval

<img width="306" height="89" alt="image" src="https://github.com/user-attachments/assets/b185d55b-8732-4d78-9c1e-491dd22730ff" />


which has length 2𝐿.

Hence,

<img width="320" height="86" alt="image" src="https://github.com/user-attachments/assets/adf7fde8-2d7a-46fc-9d16-9e1aa9ecf39d" />

Proposition (Bounded gaps contradict Sidon property)

An infinite Sidon set cannot have uniformly bounded gaps.

Proof

Assume, for contradiction, that 
<img width="364" height="88" alt="image" src="https://github.com/user-attachments/assets/a55b7d87-dd01-4289-bad6-ff91b61541aa" />

Fix a large interval [𝑥,𝑥+𝐿], and let

<img width="378" height="71" alt="image" src="https://github.com/user-attachments/assets/63ff7ac1-425d-4e06-976c-bb80672e3b56" />

By Lemma 1,

<img width="251" height="114" alt="image" src="https://github.com/user-attachments/assets/615c9bd0-0dbb-49b4-8356-ea3bd0e726d3" />

By Lemma 2, the Sidon property forces

<img width="383" height="131" alt="image" src="https://github.com/user-attachments/assets/1cbad28a-7dfe-49c5-a1b5-b334d12653c0" />

By Lemma 3, however,

<img width="343" height="124" alt="image" src="https://github.com/user-attachments/assets/938f1757-aec5-43a3-8ec2-23e890023724" />

Combining,

<img width="426" height="148" alt="image" src="https://github.com/user-attachments/assets/4e7b583f-aa57-4ccf-8995-52b82bb34292" />

which fails for sufficiently large 𝐿.

This contradiction shows that the assumption of bounded gaps is impossible. ∎

Proof of the Theorem

The proposition implies that

<img width="366" height="103" alt="image" src="https://github.com/user-attachments/assets/d61bea18-cfcd-42e9-9988-aad73e19fa34" />

Given any infinite Sidon set 𝐴, one may select a subsequence along indices where the gaps exceed 𝑛, yielding a Sidon subset with arbitrarily large gaps. ∎
