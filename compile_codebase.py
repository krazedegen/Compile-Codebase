import os
import sys
import mimetypes

# List of directories to exclude (common non-source directories)
exclude_dirs = [
    '.git', '.svn', '.hg', 'CVS',          # Version control
    'node_modules', '__pycache__',         # Dependencies and caches
    '.venv', 'venv', 'env',                # Virtual environments
    '.idea', '.vscode',                    # IDE settings
    'build', 'dist', 'target',             # Build outputs
    '.next', '.nuxt', '.cache',            # Framework-specific
    'tmp', 'temp'                          # Temporary files
]

def main(root_dir, output_file=None):
    # Check if the root directory exists and is a directory
    if not os.path.isdir(root_dir):
        print(f'Error: {root_dir} is not a directory', file=sys.stderr)
        sys.exit(1)
    
    # Open output file if specified, otherwise use stdout
    if output_file:
        try:
            output = open(output_file, 'w', encoding='utf-8')
        except Exception as e:
            print(f'Error opening output file: {e}', file=sys.stderr)
            sys.exit(1)
    else:
        output = sys.stdout
    
    # Traverse the directory tree
    for root, dirs, files in os.walk(root_dir):
        # Skip excluded directories by modifying dirs list in-place
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        for file in files:
            file_path = os.path.join(root, file)
            # Get relative path for readability in output
            rel_path = os.path.relpath(file_path, root_dir)
            # Determine if the file is text-based
            mime_type, _ = mimetypes.guess_type(file_path)
            has_no_extension = not os.path.splitext(file)[1]
            if (mime_type and mime_type.startswith('text/')) or has_no_extension:
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        # Write file separator and contents
                        print(f'----- File: {rel_path} -----', file=output)
                        for line in f:
                            print(line, end='', file=output)
                        print('\n', file=output)  # Newline after each file
                except UnicodeDecodeError:
                    print(f'Warning: Skipping {rel_path} due to encoding error', file=sys.stderr)
                except Exception as e:
                    print(f'Error reading {rel_path}: {e}', file=sys.stderr)
    
    # Close the output file if it was opened
    if output_file:
        output.close()

if __name__ == '__main__':
    # Check command-line arguments
    if len(sys.argv) < 2:
        print('Usage: python compile_codebase.py <root_dir> [output_file]', file=sys.stderr)
        sys.exit(1)
    root_dir = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    main(root_dir, output_file)
