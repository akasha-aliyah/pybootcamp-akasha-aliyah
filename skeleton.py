class CrewMember:
    def __init__(self, name, role, experience):
        self.name = name
        self.role = role
        self.experience = experience    #years of experience
    def __str__(self):
        return f"{self.name} - {self.role} ({self.experience} yrs exp)"

class CrewRoster:
    def __init__(self):
        self.crew = []      #list of CrewMember objects
    def add_member(self, name, role, experience):
        """Creates a new crew member and adds to roster."""
        self.crew.append(CrewMember(name,role,experience))
    def remove_member(self, name):
        """Removes a crew member by name."""
        for member in self.crew:
            if member.name == name:
                self.crew.remove(member)
    def list_crew(self):
        """Prints all crew members."""
        for member in self.crew:
            print(member)
            #print(member.name, end = ' ')
        #print(*self.crew, sep = ', ')

# === TEST CODE ===

roster = CrewRoster() #empty CrewRoster created

roster.add_member("Alice", "Engineer", 5)
roster.add_member("Bob", "Pilot", 10)
roster.list_crew()

print()
roster.remove_member("Alice")
roster.list_crew()
