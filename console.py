#!/usr/bin/python3

"""This module contains the entry point of the command interpreter"""

import cmd
from models import storage
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    valid_classes = ["User", "City", "State", "Place", "Review",
                     "Amenity", "BaseModel"]

    def do_create(self, line):
        """Creates a new instance of class BaseModel, and saves it to a JSON
        file, and prints the id
        """
        args_for_create = line.split()
        if len(args_for_create) == 0:
            print("** class name missing **")
        elif args_for_create[0] != "BaseModel":
            print("** class doesn't exist **")
        else:
            base_model = BaseModel()
            base_model.save()
            print(base_model.id)

    def do_show(self, line):
        """Prints the string representation of an instance based on the
        class name and id
        """
        args_for_show = line.split()

        if len(args_for_show) == 0:
            print("** class name missing **")
        elif args_for_show[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(args_for_show) < 2:
            print("** instance id missing **")
        else:
            class_name = args_for_show[0]
            uid = args_for_show[1]
            obj_key = f"{class_name}.{uid}"

            if obj_key not in storage.all().keys():
                print("** no instance found **")
            else:
                attrs = storage.all().get(obj_key)

                obj_class = globals()[class_name]
                new_instance = obj_class(**attrs)
                print(new_instance)

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id.
        The change is saved into the JSON file

        Usage: destroy <class name> <id>
        """
        args_for_destroy = line.split()

        if len(args_for_destroy) == 0:
            print("** class name missing **")
        elif args_for_destroy[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(args_for_destroy) < 2:
            print("** instance id missing **")
        else:
            class_name = args_for_destroy[0]
            uid = args_for_destroy[1]
            obj_key = f"{class_name}.{uid}"

            if obj_key not in storage.all().keys():
                print("** no instance found **")
            else:
                stored_obj = storage.all()
                stored_obj.pop(obj_key)
                storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances based
        or not on the class name

        Usage: all
               all <class name>
        """
        args_for_all = line.split()
        stored_objs = storage.all()
        print_all = []

        if len(args_for_all) > 0 and args_for_all[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            if len(args_for_all) == 0:
                for obj in stored_objs.keys():
                    obj_dict = stored_objs.get(obj)
                    obj_class = globals()[obj_dict["__class__"]]
                    new_instance = obj_class(**obj_dict)
                    print_all.insert(0, new_instance.__str__())
                print(print_all)
            else:
                if args_for_all[0] not in self.valid_classes:
                    print("** class doesn't exist **")
                else:
                    class_name = args_for_all[0]
                    obj_class = globals()[class_name]
                    for obj in stored_objs.keys():
                        if obj.startswith(class_name):
                            obj_dict = stored_objs.get(obj)
                            new_instance = obj_class(**obj_dict)
                            print_all.insert(0, new_instance.__str__())
                    print(print_all)

    def do_update(self, line):
        """Updates an attribute or adds a new attribute to an existing instance
        of a valid class and saves the change to the JSON file.

        Usage: update <class name> <id> <attribute name> <attribute value>
        """
        args_for_update = line.split()
        stored_objs = storage.all()

        if len(args_for_update) == 0:
            print("** class name missing **")
        elif args_for_update[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(args_for_update) < 2:
            print("** instance id missing **")
        else:
            class_name = args_for_update[0]
            uid = args_for_update[1]
            obj_key = f"{class_name}.{uid}"

            if obj_key not in stored_objs.keys():
                print("** no instance found **")
            elif len(args_for_update) < 3:
                print("** attribute name missing **")
            elif len(args_for_update) < 4:
                print("** value missing **")
            else:
                attr_name = args_for_update[2]
                attr_value = args_for_update[3]
                obj_dict = stored_objs.get(obj_key)

                if attr_name in obj_dict.keys():
                    value_type = type(obj_dict.get(attr_name))
                    obj_dict[attr_name] = value_type(attr_value)
                else:
                    obj_dict[attr_name] = attr_value

                obj_class = globals()[class_name]
                new_instance = obj_class(**obj_dict)
                new_instance.save()

    def do_quit(self, line):
        """Exits the command interpreter"""
        return True

    def do_EOF(self, line):
        """Exits the command interpreter when an EOF condition is passed"""
        return True

    def emptyline(self):
        """Overrides repeating the last nonempty command after an empty
        line is entered"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
