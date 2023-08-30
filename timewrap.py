# Import Necessary Packages
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import numpy as np


def create_compressed_timeline(events, total_hours=24):

    years = list(events.keys())
    start_time = datetime(year=1, month=1, day=1, hour=0, minute=0, second=0)
    end_time = start_time + timedelta(hours=total_hours)
    time_range = end_time - start_time

    compressed_timeline = []
    for year in years:
        event_time = start_time + ((year - min(years)) / (max(years) - min(years))) * time_range
        compressed_timeline.append({
            'year': year,
            'event_name': events[year],
            'compressed_time': event_time
        })
    
    return compressed_timeline

def print_time_differences(compressed_timeline):

    compressed_timeline.sort(key=lambda x: x['year'])
    for i in range(1, len(compressed_timeline)):
        event_a = compressed_timeline[i - 1]
        event_b = compressed_timeline[i]
        time_difference = (event_b['compressed_time'] - event_a['compressed_time']).seconds // 3600
        if time_difference == 0:
            time_difference = ((event_b['compressed_time'] - event_a['compressed_time']).seconds % 3600)//60
            print(f"{event_b['event_name']} occurred after {time_difference} minutes from {event_a['event_name']} !!")
        else:
            print(f"{event_b['event_name']} occurred after {time_difference} hours from {event_a['event_name']} !!")

def print_output(compressed_timeline):
    for i in range(1, len(compressed_timeline)):
        print(compressed_timeline[i-1]['event_name'],compressed_timeline[i-1]['compressed_time'].strftime('%H:%M'))

def visualize_compressed_timeline_line(compressed_timeline):

    compressed_timeline.sort(key=lambda x: x['compressed_time'])

    fig, ax = plt.subplots(figsize=(12, 3))
    plt.plot([0, 24], [0, 0], color='black', linewidth=2)
    
    for event in compressed_timeline:
        event_hour = event['compressed_time'].hour + event['compressed_time'].minute / 60
        ax.scatter(event_hour, 0, marker='o', s=200, color='blue')
        ax.annotate(event['event_name'], xy=(event_hour, 0), xytext=(1, 8), textcoords='offset points', ha='center', va='bottom', rotation=90, color='black')
    
    ax.set_xlim(0, 24)
    ax.set_xticks(range(25))
    ax.set_xlabel('Time (hours)')

    ax.set_ylim(-0.05, 0.05)
    ax.set_yticks([])
    
    plt.title('Compressed Timeline : if all events happened in 24 hours')
    plt.show()

input_events = {
   1951:"Magnetic Tape",
   1955:"Magnetic Disk",
   1961:"ISAM",
   1965:"Hierarchical Model",
   1968:"IMS",
   1969:"Network Model",
   1970:"Codd's Paper",
   1971:"IDMS",
   1974:"System R",
   1978:"Oracle",
   1984:"DB2",
   1989:"Postgres and SQL server",
   1995:"MySQL",
   2003:"Marklogic",
   2004:"MapReduce",
   2005:"Hadoop",
   2007:"Dynamo",
   2008:"Cassandra, Hbase, NuoDB",
   2009:"MongoDB"
}

print("The Timeline:",input_events)
print("\n")
print("If this time was compressed to one day this is when major events would occur!")
compressed_timeline = create_compressed_timeline(input_events)
print_output(compressed_timeline)
print("\n")
print("We can Now see relatively how long it took for new things to come up! \n")
print_time_differences(compressed_timeline)
visualize_compressed_timeline_line(compressed_timeline)