def generate_class_template():
    # Returns a string containing a basic public class template
    return "public class ClassName {\n\t\n}"

def generate_main_method_template():
    # Returns a string containing a basic public static void main method template
    return "public static void main(String[] args) {\n\t\n}"

def generate_for_loop_template():
    # Returns a string containing a basic for loop template
    return "for (int i = 0; i<; i++) {\n\t\n}"

def generate_while_loop_template():
    # Returns a string containing a basic while loop template
    return "while (condition) {\n\t\n}"

def generate_switch_template():
    # Returns a string containing a basic switch statement template
    return "switch (variable) {\n  case value1:\n    // code here\n    break;\n  case value2:\n    // code here\n    break;\n  default:\n    // code here\n    break;\n}"

def generate_if_template():
    # Returns a string containing a basic if statement template
    return "if (condition) {\n  \t  // code here\n}"

def generate_else_if_template():
    # Returns a string containing a basic else-if statement template
    return "else if (condition) {\n  \t  // code here\n}"

def generate_else_template():
    # Returns a string containing a basic else statement
    return "else {\n    // code here\n}"

def generate_try_template():
    # Returns a string containing a basic try template
    return "try {\n    // code here\n}"

def generate_catch_template():
    # Returns a string containing a basic catch template
    return "catch (Exception e) {\n    // code here\n}"

def generate_try_catch_template():
    # Returns a string containing a basic try-catch template
    return "try {\n    // code here\n} catch (Exception e) {\n    // code here\n}"

def generate_try_catch_finally_template():
    # Returns a string containing a basic try-catch template
    return "try {\n    // code here\n} catch (Exception e) {\n    // code here \n} \n finally {\n //code here \n}"

def generate_print_template():
    # Returns a string containing a basic print statement template
    return "System.out.println(\"text to print\");\n"

def generate_interface_template():
    # Returns a string containing a basic public interface template
    return "public interface InterfaceName {\n\n}"

def generate_enhanced_for_loop_template():
    # Returns a string containing a basic enhanced for loop template
    return "for (type variable : collection) {\n    // code here\n}"

def generate_do_while_loop_template():
    # Returns a string containing a basic do-while loop template
    return "do {\n    // code here\n} while (condition);"

def generate_constructor_template():
    # Returns a string containing a basic constructor template
    return "public ClassName() {\n    // code here\n}"

def generate_parameterized_constructor_template():
    # Returns a string containing a basic parameterized constructor template
    return "public ClassName(arg1Type arg1, arg2Type arg2) {\n    // code here\n}"

def generate_setter_template():
    # Returns a string containing a basic setter method template
    return "public void setVariableName(variableType variable) {\n    this.variable = variable;\n}"

def generate_getter_template():
    # Returns a string containing a basic getter method template
    return "public variableType getVariableName() {\n    return variable;\n}"

def generate_synchronized_setter_template():
    # Returns a string containing a basic setter method template
    return "public synchronized void setVariableName(variableType variable) {\n    this.variable = variable;\n}"

def generate_synchronized_getter_template():
    # Returns a string containing a basic getter method template
    return "public synchronized variableType getVariableName() {\n    return variable;\n}"

def generate_abstract_class_template():
    # Returns a string containing an abstract class template
    return "public abstract class AbstractClassName {\n// Abstract methods go here \n}"

def generate_synchronized_method_template():
    # Returns a string containing an synchronized method template
    return "synchronized void synchronisedMethodName(){\n//synchronized method  \n}"

def generate_method_template():
    # Returns a string containing a method template
    return "public void methodName(){\n//method  \n}"

def generate_static_method_template():
    # Returns a string containing a static method template
    return "public static void staticMethodName(){\n// static method  \n}"

def generate_class_main_template():
    # Returns a string containing a class and a main template
    return "public class ClassName {\n  public static void main(String args[]){ \n}\n}"



template_mapping = {
    "class main method":generate_class_main_template,
    "class": generate_class_template,
    "main method": generate_main_method_template,
    "for": generate_for_loop_template,
    "while": generate_while_loop_template,
    "switch": generate_switch_template,
    "else if": generate_else_if_template,
    "if": generate_if_template,
    "else": generate_else_template,
    "try catch finally": generate_try_catch_finally_template,
    "try catch": generate_try_catch_template,
    "try": generate_try_template,
    "print": generate_print_template,
    "interface": generate_interface_template,
    "enhanced": generate_enhanced_for_loop_template,
    "do while": generate_do_while_loop_template,
    "default constructor": generate_constructor_template,
    "parametrized constructor": generate_parameterized_constructor_template,
    "parameterized constructor": generate_parameterized_constructor_template,
    "setter": generate_setter_template,
    "getter": generate_getter_template,
    "synchronized setter": generate_synchronized_setter_template,
    "synchronized getter": generate_synchronized_getter_template,    
    "method":generate_method_template,
    "static method":generate_static_method_template,
    "synchronized method":generate_synchronized_method_template,
    "abstract class":generate_abstract_class_template,
}
