fn eratosthenes<T>(n: T) -> Vec<T>
where
    T: Copy
        + TryInto<usize>
        + TryFrom<usize>
        + std::ops::Rem<Output = T>
        + std::cmp::PartialOrd
        + std::ops::Add<Output = T>
        + std::ops::Mul<Output = T>
        + std::marker::Sized,
{
    let n_usize: usize = match n.try_into() {
        Ok(num) => num,
        Err(_) => return Vec::new(),
    };

    let mut is_prime = vec![true; n_usize + 1];
    is_prime[0] = false;
    is_prime[1] = false;

    let mut primse: Vec<T> = Vec::new();

    for (i, &p) in is_prime.iter().skip(1).enumerate() {
        if !p {
            continue;
        }

        match T::try_from(i) {
            Ok(val) => primse.push(val),
            Err(_) => break,
        }
    }
    primse
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        let result = eratosthenes(10);
        assert_eq!(result, vec![2, 3, 5, 7]);
    }
}
