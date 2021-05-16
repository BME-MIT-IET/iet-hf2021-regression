import java.util.Random;

/*
* Bogosort is highly inefficient sorting algorithm based on generate and test paradigm.
*/
public class Bogosort {
    public static void main(String[] args) {
        if (args.length == 1) {
            String[] arr = args[0].split(",");
            Integer[] intArr = new Integer[arr.length];

            for (int i = 0; i < arr.length; i++) {
                intArr[i] = Integer.parseInt(arr[i]);
            }

            sort(intArr);

            for (int i = 0; i < arr.length; i++) {
                arr[i] = intArr[i].toString();
            }

            Logger.log(String.join(", ", arr));

        } else {
            Logger.log("An array needs to be passed in!");
        }
    }

    public static boolean isSorted(Integer[] arr) {
        /*
         * Function which checks if array is sorted.
         */
        for (int i = 1; i < arr.length; i++) {
            if (arr[i - 1] > arr[i]) {
                return false;
            }
        }
        return true;
    };

    public static Integer[] shuffle(Integer[] arr) {
        /*
         * Shuffle function swaps random array elements
         */
        String[] strArr = new String[arr.length];
        Integer count = arr.length, temp, index;
        Random rand = new Random();

        while (count > 0) {
            index = rand.nextInt() * count;
            count--;

            temp = arr[count];
            arr[count] = arr[index];
            arr[index] = temp;
        }
        return arr;
    }

    public static Integer[] sort(Integer[] arr) {
        boolean sorted = false;
        while (!sorted) {
            shuffle(arr);
            sorted = isSorted(arr);
        }
        return arr;
    }
}
