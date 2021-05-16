
public class Interpolation {

	public static int interpolationSearch(int x, int[] arr) {
		// Find indexes of two corners

		int low = 0;
		int high = (arr.length - 1);

		// Since array is sorted, an element present
		// in array must be in range defined by corner
		while (low <= high && x >= arr[low] && x <= arr[high]) {
			int pos = low + (((high - low) / (arr[high] - arr[low])) * (x - arr[low]));

			if (arr[pos] == x)
				return pos;

			if (arr[pos] < x)
				low = pos + 1;

			else
				high = pos - 1;
		}
		return -1;
	}

	public static void main(String[] args) {
		int x = 20;
		int[] arr = new int[] { 10, 12, 13, 15, 17, 19, 20, 21, 22, 23, 24, 33, 35, 42, 49 };
		int index = interpolationSearch(x, arr);

		// If element was found
		if (index != -1)
			Logger.log("Element found at index " + index);
		else
			Logger.log("Element not found.");
	}
}
