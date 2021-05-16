import java.util.InputMismatchException;
import java.util.Scanner;
import java.util.Stack;

public class TopologicalSort {

    private Deque<Integer> stack;

    public TopologicalSort() {
        stack = new Deque<Integer>();
    }

    public int[] topological(int adjacency_matrix[][], int source) throws NullPointerException {
        int number_of_nodes = adjacency_matrix[source].length - 1;
        int[] topological_sort = new int[number_of_nodes + 1];
        int pos = 1;
        int j;
        int visited[] = new int[number_of_nodes + 1];
        int element = source;
        int i = source;
        visited[source] = 1;
        stack.push(source);

        while (!stack.isEmpty()) {
            element = stack.peek();
            while (i <= number_of_nodes) {
                if (adjacency_matrix[element][i] == 1 && visited[i] == 1 && stack.contains(i)) {
                    Logger.log("TOPOLOGICAL SORT NOT POSSIBLE");
                    throw new NullPointerException();

                }
                if (adjacency_matrix[element][i] == 1 && visited[i] == 0) {
                    stack.push(i);
                    visited[i] = 1;
                    element = i;
                    i = 1;
                    continue;
                }
                i++;
            }
            j = stack.pop();
            topological_sort[pos++] = j;
            i = ++j;
        }
        return topological_sort;
    }

    public static void main(String... arg) {
        int number_no_nodes, source;
        Scanner scanner = null;
        int topological_sort[] = null;
        try {
            Logger.log("Enter the number of nodes in the graph");
            scanner = new Scanner(System.in);
            number_no_nodes = scanner.nextInt();

            int adjacency_matrix[][] = new int[number_no_nodes + 1][number_no_nodes + 1];
            Logger.log("Enter the adjacency matrix");
            for (int i = 1; i <= number_no_nodes; i++)
                for (int j = 1; j <= number_no_nodes; j++)
                    adjacency_matrix[i][j] = scanner.nextInt();

            Logger.log("Enter the source for the graph");
            source = scanner.nextInt();

            Logger.log("The Topological sort for the graph is given by ");
            TopologicalSort toposort = new TopologicalSort();
            topological_sort = toposort.topological(adjacency_matrix, source);

            for (int i = topological_sort.length - 1; i > 0; i--) {
                if (topological_sort[i] != 0)
                    Logger.log(topological_sort[i] + "\t");
            }
        } catch (InputMismatchException inputMismatch) {
            Logger.log("Wrong Input format");
        } catch (NullPointerException nullPointer) {
        }
        scanner.close();
    }
}
