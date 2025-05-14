#include <string.h>
#include <stdint.h>
#include <stdio.h>

int check(const char *param_1) {
    size_t sVar1 = strlen(param_1);
    if (sVar1 != 0x1b) { // 27バイトでなければ失敗
        return 1;
    }

    // local_58の値（23バイト）
    uint8_t local_58[23] = {
        0xe1, 0xa7, 0x1e, 0xf8, 0x75, 0x23, 0x7b, 0x61,
        0xb9, 0x9d, 0xfc, 0x5a, 0x5b, 0xdf, 0x69, 0xd2,
        0xfe, 0x1b, 0xed, 0xf4, 0xed, 0x67, 0xf4
    };

    int bit_index = 0; // 入力パスワードのビット位置
    for (int i = 0; i < 23; i++) {      // local_58の各バイト
        for (int j = 0; j < 8; j++) {   // 各ビット
            int pass_byte = bit_index / 8;
            int pass_bit  = 7 - (bit_index % 8);

            int pass_bit_val = (param_1[pass_byte] >> pass_bit) & 1;
            int ref_bit_val  = (local_58[i] >> (7 - j)) & 1;

            if (pass_bit_val != ref_bit_val) {
                return 1; // 不一致
            }
            bit_index++;
            if (bit_index >= 27*8) break; // 念のため
        }
    }
    return 0; // 一致
}


int main(void) {
    char local_118[0x100] = {0};  // 256バイトのバッファを0初期化

    printf("Enter the password: ");
    fgets(local_118, 0x100, stdin);

    // fgetsで改行が入るので消す
    size_t len = strlen(local_118);
    if (len > 0 && local_118[len-1] == '\n') {
        local_118[len-1] = '\0';
    }

    if (check(local_118) == 0) {
        puts("Correct!! :D");
        return 0;
    } else {
        puts("Wrong :(");
        return 1;
    }
}