# (PasswordGenerator) 
Tested on linux

Singleton and builder pattern rough implementation

Configuration file available at ~/.passwdgen/passwdgen.profile

Usage:
python3 ./main.py [options]

```text
python3 ./main.py --help 
          --help - this help 
          --length=n - the password length 
          --no-lower - don't use lowercase characters 
          --no-upper - don't use uppercase characters 
          --no-numbers - don't use digits 
          --no-specials - don't use special characters 
          --min-lower=n - minumum number of lowercase chars the password will contain 
          --min-upper=n - minumum number of uppercase chars the password will contain 
          --min-numbers=n - minumum number of digits the password will contain 
          --min-specials=n - minumum number of special chars the password will contain 
          --with-letters=str - set the lowercase and uppercase alphabet (could require escaping \xxx) 
          --with-lower=str - set the lowercase alphabet (could require escaping \xxx) 
          --with-upper=str - set the uppercase alphabet (could require escaping \xxx) 
          --with-numbers=str - set the vailables digits (could require escaping \xxx) 
          --with-specials=str - set the special chars string (could require escaping \xxx) 
```
## examples
**password length=15 with a number, 2 uppercase letters and a special symbol**
python3 ./main.py -l 15 --min-numbers=1 --min-upper=2 --min-specials=1
```text
Parameters in use:
        lower==>ekmhvbcwtfxrsngqajyzoulipd
        upper==>ZLIFNVEOARCQJMSWYXKDTHUPBG
        numbers==>4182703695
        specials==>$?-+#@_
        complete==>yAwCRPNusafeq#D93Yc8X-@$SpgMoz0jkHElLxJrFn4+B1QWdGUtViIT_76bOv5mh?Z2K
        Minimum number of uppercase=2
        Minimum number of numbers=1
        Minimum number of special character=1

g_X803t9aPX0TAC
```

***greek alphabet***
python3 ./main.py -l 15 --with-letters="αβγδεζηθικλμνξοπρστυφχψω"
```text
Parameters in use:
        lower==>βωνπεημαιθψξτκζυρσχδφολγ
        upper==>ΔΡΠΗΝΤΩΨΧΚΖΥΞΦΓΕΙΟΒΜΘΣΛΑ
        numbers==>4632957018
        specials==>@-$?#_+
        complete==>ψφ#$ΔΤ7μ1ΧΛχλσζΥ8ιΑΚ5ρΞ+Ε@απεωΜΖ2ΘνυΠ?-ξ6ΓβΦΝ90κδ4Ρ_θτΙΣΩΗγΨ3οηΟΒ

θΖμ4ωΡΔΥΕ?@σ_γ8
```

***cyrillic alphabet***
python3 ./main.py -l 15 --with-letters="абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
```text
Parameters in use:
        lower==>тячаьлрдмсошфбепэжыюквуйищзнцъгхё
        upper==>ЦБЩУИОЁЮЗЙРШЪГЕВДХЖАТЧНЫФКЭЬЛМЯСП
        numbers==>0893527641
        specials==>@+_#$-?
        complete==>1?6+хиэЧучЯ@ва7лУ0ёВ#ЦЪАйЕ9-МЙьпдБю2е5ОЭ4ДыТФ$сШжПбИфХЁзятъогЬЖЛКРм8Зн_рСшГкЮцЩщН3Ы

я9Л-этЮЦФ91г8ЕЛ
```

***reduced lowercase set***
python3 ./main.py -l 15 --with-letters="christmas" --no-upper
```text
Parameters in use:
        lower==>hraicsmst
        upper==>None
        numbers==>8275901436
        specials==>_#$-+@?
        complete==>it54h-e6s+8o#07?s2m1@9cn3arN_$

23trs87--+mei32
```
