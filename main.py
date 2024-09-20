def chery_seed2key(seed: int) -> int:
    seed_list = (seed >> 8, seed & 0xFF)
    temp = seed_list[0]
    result = 0xFFFE

    for seed_idx in range(2):
        result = (result & 0xFFFF) ^ (seed_list[seed_idx] << 8)

        for _ in range(8):
            if result & 0x8000:
                temp = (result & 0xffff) << 1
                if result & 0x80:
                    result = temp ^ 0x8408
                else:
                    result = temp ^ 0x8025
            else:
                result = (result & 0xffff) << 1

    return result & 0xFFFF


def main():
    seeds = [0x41C6, 0x1D6F, 0x0149, 0x3E7C, 0xE75E]
    [print(f"seed: {hex(seed)} -> key: {hex(chery_seed2key(seed))}") for seed in seeds]


if __name__ == "__main__":
    main()