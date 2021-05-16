package org.opengenus.cosmos.search;

class TernarySearch {

    public static int search(String[] x, String target, int start, int end) {

        if (start < end) {
            int midpoint1 = start + (end - start) / 3;
            int midpoint2 = start + 2 * (end - start) / 3;
            if (target.compareTo(x[midpoint1]) == 0) {
                return midpoint1;
            } else if (target.compareTo(x[midpoint2]) == 0) {
                return midpoint2;
            } else if (x[midpoint1].compareTo(x[midpoint2]) < 0) {
                return search(x, target, midpoint1, end);
            } else {
                return search(x, target, start, midpoint2);
            }
        }

        return -1;
    }

    public static void main(String[] args) {
        // declare a string array with initial size

        String[] songs = { "Ace", "Space", "Diamond" };

        Logger.log("\nTest binary (String):");
        Logger.log(search(songs, "Ace", 0, 3));

    }
}
