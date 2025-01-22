### Why Does `if complement in seen:` Perform in \( O(1) \)?

#### **1. Dictionaries Use Hash Tables**
- Python dictionaries are implemented as **hash tables**, which allow for efficient key lookups.
- The key (`complement`) is hashed using a hash function, and the hash determines where the key is stored in memory.

---

#### **2. Steps in Lookup**
1. **Hashing**: Compute the hash of `complement` using `hash()`.  
2. **Find the Bucket**: Use the hash to locate the corresponding "bucket" in the hash table.  
3. **Compare Keys**: If there are multiple keys in the bucket (rare), compare `complement` with them to find the exact match.

---

#### **3. Why \( O(1) \)?**
- **Hashing**: Calculating the hash takes constant time.
- **Bucket Lookup**: Accessing a memory location is \( O(1) \).
- **Key Comparison**: Comparing keys is very fast in most cases.

---

#### **4. Collisions**
- A collision happens when two keys have the same hash and are stored in the same bucket.
- In such cases, Python resolves collisions using chaining (storing multiple entries in a single bucket).
- While worst-case complexity can degrade to \( O(n) \), Python's hash function minimizes collisions, so the average case remains \( O(1) \).

---

#### **5. Summary**
- **Average Case**: \( O(1) \), due to efficient hashing and lookup mechanisms.
- **Worst Case**: \( O(n) \), if many collisions occur (rare in practice).
