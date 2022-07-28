using System;

internal class Mutation {
	public static readonly int KeyI0 = 3;
	public static readonly int KeyI1 = 4;
	public static readonly int KeyI2 = 5;
	public static readonly int KeyI3 = 6;
	public static readonly int KeyI4 = 7;
	public static readonly int KeyI5 = 8;
	public static readonly int KeyI6 = 9;
	public static readonly int KeyI7 = 10;
	public static readonly int KeyI8 = 11;
	public static readonly int KeyI9 = 12;
	public static readonly int KeyI10 = 13;
	public static readonly int KeyI11 = 14;
	public static readonly int KeyI12 = 15;
	public static readonly int KeyI13 = 16;
	public static readonly int KeyI14 = 17;
	public static readonly int KeyI15 = 18;

	public static T Placeholder<T>(T val) {
		return val;
	}

	public static T Value<T>() {
		return default(T);
	}

	public static T Value<T, Arg0>(Arg0 arg0) {
		return default(T);
	}

	public static void Crypt(uint[] data, uint[] key) { }
}