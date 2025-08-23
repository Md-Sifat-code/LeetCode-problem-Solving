from graphviz import Digraph

# Create DFD like the user's example (Food Ordering System style)
dfd2 = Digraph("CityGuidePlusDFD", format="png")
dfd2.attr(rankdir="LR", size="10")

# External Entities
dfd2.node("User", "User", shape="rectangle", style="filled", color="lightyellow")
dfd2.node("TicketService", "Ticketing Service", shape="rectangle", style="filled", color="lightyellow")
dfd2.node("Payment", "Payment Channel", shape="rectangle", style="filled", color="lightyellow")

# Processes (rounded rectangles with numbers)
dfd2.node("P1", "1\nLogin / Manage Account", shape="rectangle", style="rounded,filled", color="lightblue")
dfd2.node("P2", "2\nExplore Attractions & Personalize", shape="rectangle", style="rounded,filled", color="lightblue")
dfd2.node("P3", "3\nBook Event Ticket", shape="rectangle", style="rounded,filled", color="lightblue")
dfd2.node("P4", "4\nProcess Payment", shape="rectangle", style="rounded,filled", color="lightblue")
dfd2.node("P5", "5\nSend Notifications", shape="rectangle", style="rounded,filled", color="lightblue")

# Data Stores (D)
dfd2.node("D1", "D1\nUSER File", shape="box3d", style="filled", color="lightgrey")
dfd2.node("D2", "D2\nLOCATION DB", shape="box3d", style="filled", color="lightgrey")
dfd2.node("D3", "D3\nEVENT_TICKET DB", shape="box3d", style="filled", color="lightgrey")

# Connections similar to Food Ordering style
dfd2.edge("User", "P1", "Login Data")
dfd2.edge("P1", "User", "Access Response")
dfd2.edge("P1", "D1", "Auth Data")
dfd2.edge("User", "P2", "Search/Browse/Favorites")
dfd2.edge("P2", "D2", "Attraction/Event Data")
dfd2.edge("User", "P3", "Event Selection")
dfd2.edge("P3", "TicketService", "Booking Request")
dfd2.edge("TicketService", "P3", "Availability/Confirmation")
dfd2.edge("P3", "D3", "Booking Record")
dfd2.edge("User", "P4", "Payment Initiation")
dfd2.edge("P4", "Payment", "Payment Request")
dfd2.edge("Payment", "P4", "Payment Status")
dfd2.edge("P4", "D3", "Update Payment Status")
dfd2.edge("D3", "P5", "Booking Updates")
dfd2.edge("D2", "P5", "Event Updates")
dfd2.edge("P5", "User", "Notifications")

# Render
output_path2 = "/output"
dfd2.render(output_path2, cleanup=True)
output_path2 + ".png"
