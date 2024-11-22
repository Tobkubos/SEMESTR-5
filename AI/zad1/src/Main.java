

import net.sourceforge.jFuzzyLogic.FIS;
import net.sourceforge.jFuzzyLogic.plot.JFuzzyChart;
import net.sourceforge.jFuzzyLogic.rule.Variable;

public class Main {
    public static void main(String[] args) throws Exception {
        // Load from 'FCL' file
        String fileName = "FCL/TobiaszKubiak_1.fcl";
        FIS fis = FIS.load(fileName,true);

        // Error while loading?
        if( fis == null ) {
            System.err.println("Can't load file: '" + fileName + "'");
            return;
        }

        // Show
        JFuzzyChart.get().chart(fis);

        // Set inputs
        fis.setVariable("predkosc_jazdy", 130);
        fis.setVariable("widocznosc", 0.9);

        // Evaluate
        fis.evaluate();

        // Show output variable's chart
        Variable crash = fis.getVariable("prawdopodobienstwo_wypadku");
        JFuzzyChart.get().chart(crash, crash.getDefuzzifier(), true);

        // Print ruleSet
        System.out.println(fis);
    }
}