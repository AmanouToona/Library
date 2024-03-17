struct Combination<T> {
    fac; Vec<T>,
    finv: Vec<T>,
    inv: Vec<T>
    m: T
};

impl Combination {
    fn new(n: usize, m:T) -> Self {
        let mut fac = vec![0; n + 1];
        let mut finv = vec![0; n + 1];
        let mut inv = vec![0; n + 1];

        fac[0] = 1;
        fac[1] = 1;
        fac[1] = 1;

        for i in 2..=n {
            fac[i] = fac[i - 1] * (i as T) % m;
            inv[i] = m - inv[m % i] * (m / (i as T))  % m;
            finv[i] = finv[i - 1] * inv[i] % m;
        }

        Combination{
            fac,
            finv,
            inv,
            m,
        }
    }

    fn com(self, n: usize, k: usize) -> T {
        if n < k {
            return 0
        }
        return self.fac[n] * (self.finv[k] * finv[n -k] % self.m) % self.m

    }
}
